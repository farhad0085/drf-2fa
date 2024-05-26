class DRF2FAException(Exception):
    default_msg = None

    def __init__(self, msg=None, *args, **kwargs):
        print(msg)
        if not msg:
            msg = self.default_msg
        super().__init__(msg, *args, **kwargs)

class InvalidPhoneNumberField(DRF2FAException):
    default_msg = "Couldn't retrieve user's phone number to send message. Please check `PHONE_NUMBER_FIELD` settings."    

class SMSCouldNotSend(DRF2FAException):
    default_msg = "SMS Couldn't send to user's phone number, please check the credentials."

class SMSClientCouldNotCreate(DRF2FAException):
    default_msg = "SMS Client couldn't create, please check credentials"
