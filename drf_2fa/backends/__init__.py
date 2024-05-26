import string, random
from drf_2fa.models import OTPCode
from drf_2fa.settings import drf_2fa_settings


class BaseOTPBackend:

    def __init__(self):
        self.settings = self.get_settings()
    
    def get_settings(self):
        return drf_2fa_settings

    def generate_otp(self):
        otp_code = ''.join(random.choices(string.digits, k=drf_2fa_settings.OTP_LENGTH))
        return otp_code

    def verify_otp(self, user, otp):
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `verify_otp` method")
    
    def save_otp(self, user):
        """store otp in database if required"""
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `save_otp` method")
    
    def send_otp(self, user, otp_code):
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

