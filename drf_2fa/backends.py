import string, random
from drf_2fa.models import OTPCode
from drf_2fa.settings import drf_2fa_settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


class BaseOTPBackend:

    def generate_otp(self):
        otp_code = ''.join(random.choices(string.digits, k=drf_2fa_settings.OTP_LENGTH))
        return otp_code

    def verify_otp(self, user, otp):
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `verify_otp` method")
    
    def save_otp(self, user):
        """store otp in database if required"""
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `save_otp` method")
    
    def send_otp(self, user):
        """This method is responsible to send the otp to user"""
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `send_otp` method")

    def save_and_send_otp_code(self, user):
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `save_and_send_otp_code` method")


class BaseMessageOTPBackend(BaseOTPBackend):

    def verify_otp(self, user, otp):
        is_valid, otp_obj = OTPCode.is_valid(user, otp)
        if is_valid:
            otp_obj.delete() # delete otp from the database, since it's already used and verified
        return is_valid

    def save_otp(self, user):
        otp_code = self.generate_otp()
        # save the otp to database
        OTPCode.objects.create(user=user, otp_code=otp_code)
        return otp_code

    def save_and_send_otp_code(self, user):
        otp_code = self.save_otp(user)
        self.send_otp(user, otp_code)


class EmailOTPBackend(BaseMessageOTPBackend):
    """Send OTP in user's email"""

    def send_otp(self, user, otp_code):
        subject = render_to_string('drf_2fa/email/subject.txt')
        email_content = render_to_string('drf_2fa/email/message.html', {'otp_code': otp_code})

        send_mail(
            subject=subject,
            message=email_content,
            from_email=drf_2fa_settings.OTP_EMAIL_FROM,
            recipient_list=[user.email]
        )
