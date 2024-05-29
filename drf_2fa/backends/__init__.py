import string, random
from drf_2fa.models import OTPCode
from drf_2fa.settings import drf_2fa_settings
from django.template.loader import render_to_string


class BaseOTPBackend:
    """
    Base class for OTP backends.

    This class defines the interface for OTP backends and provides common methods
    that must be implemented by subclasses.

    Subclasses must implement the following methods:
        - `verify_otp(user, otp)`
        - `save_otp(user)`
        - `send_otp(user)`
        - `save_and_send_otp_code(user)`
    """

    def __init__(self):
        self.settings = self.get_settings()
        self.otp_code = None
    
    def get_settings(self):
        """Get DRF 2FA settings."""
        return drf_2fa_settings

    def generate_otp(self):
        """Generate a random OTP code."""
        if getattr(self, 'otp_code'):
            return self.otp_code
        else:
            self.otp_code = ''.join(random.choices(string.digits, k=drf_2fa_settings.OTP_LENGTH))
        return self.otp_code

    def verify_otp(self, user, otp):
        """Verify the OTP code."""
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `verify_otp` method")
    
    def save_otp(self, user):
        """store the OTP in database if required"""
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `save_otp` method")
    
    def send_otp(self, user):
        """Send the OTP to the user."""
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `send_otp` method")

    def save_and_send_otp_code(self, user):
        """Save and send the OTP code."""
        raise NotImplementedError(f"`{self.__class__.__name__}` backend must override `save_and_send_otp_code` method")


class BaseMessageOTPBackend(BaseOTPBackend):
    """
    Base class for message-based OTP backends.

    This class extends `BaseOTPBackend` and provides methods specific to message-based OTPs.
    """

    template_name = "drf_2fa/sms/message.txt"

    def get_context_data(self):
        """Get the context data for rendering the message template."""
        return {}
    
    def get_message_content(self):
        """Get the message content."""
        context = self.get_context_data()
        return render_to_string(self.template_name, context=context)

    def verify_otp(self, user, otp):
        """Verify the OTP code."""
        is_valid, otp_obj = OTPCode.is_valid(user, otp)
        if is_valid:
            otp_obj.delete() # delete otp from the database, since it's already used and verified
        return is_valid

    def save_otp(self, user):
        """Save the OTP in the database."""
        otp_code = self.generate_otp()
        # save the otp to database
        OTPCode.objects.create(user=user, otp_code=otp_code)
        return otp_code

    def save_and_send_otp_code(self, user):
        """Save and send the OTP code to the user"""
        self.save_otp(user)
        self.send_otp(user)


class SMSOTPBackend(BaseMessageOTPBackend):
    """
    Base class for sms-based OTP backends.

    This class extends `BaseMessageOTPBackend` and provides methods specific to sms-based OTPs.
    """
    pass
