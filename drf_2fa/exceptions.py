class DRF2FAException(Exception):
    """
    Base exception class for DRF 2FA
    """
    default_msg = None

    def __init__(self, msg=None, *args, **kwargs):
        if not msg:
            msg = self.default_msg
        super().__init__(msg, *args, **kwargs)

class InvalidPhoneNumberField(DRF2FAException):
    """
    Exception raised when a user's phone number cannot be retrieved to send an SMS message.
    """
    default_msg = "Couldn't retrieve user's phone number to send message. Please check `PHONE_NUMBER_FIELD` settings."    


class SMSCouldNotSend(DRF2FAException):
    """
    Exception raised when an SMS could not be sent to the user's phone number.
    """
    default_msg = "SMS Couldn't send to user's phone number, please check the credentials."


class SMSClientCouldNotCreate(DRF2FAException):
    """
    Exception raised when an SMS client could not be created.
    """
    default_msg = "SMS Client couldn't create, please check credentials"
