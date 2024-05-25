import string, random
from drf_2fa.models import OTPCode
from drf_2fa.settings import drf_2fa_settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


class BaseOTPBackend:

    def verify_otp(self, user, otp):
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `verify_otp` method")
    
    def generate_otp(self, user):
        """This method generates otp and store in database if required"""
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `generate_otp` method")
    
    def send_otp(self, user):
        """This method is responsible to send the otp to user"""
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `send_otp` method")

    def generate_and_send_code(self, user):
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `generate_and_send_code` method")


class EmailOTPBackend(BaseOTPBackend):

    def verify_otp(self, user, otp):
        is_valid, otp_obj = OTPCode.is_valid(user, otp)
        if is_valid:
            otp_obj.delete() # delete otp from the database, since it's already used and verified
        
        return is_valid

    def generate_otp(self, user):
        self.otp_code = ''.join(random.choices(string.digits, k=drf_2fa_settings.OTP_LENGTH))
        # save the otp to database
        OTPCode.objects.create(user=user, otp_code=self.otp_code)
        return self.otp_code

    def send_otp(self, user):
        subject = render_to_string('drf_2fa/email/subject.txt')
        email_content = render_to_string('drf_2fa/email/message.html', {'otp_code': self.otp_code})

        send_mail(
            subject=subject,
            message=email_content,
            from_email=drf_2fa_settings.OTP_EMAIL_FROM,
            recipient_list=[user.email]
        )

    def generate_and_send_code(self, user):
        self.generate_otp(user)
        self.send_otp(user)
