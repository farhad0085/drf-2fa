from twilio.rest import Client
from drf_2fa.backends import SMSOTPBackend
from twilio.base.exceptions import TwilioRestException
from drf_2fa.exceptions import InvalidPhoneNumberField, SMSClientCouldNotCreate, SMSCouldNotSend


class TwilioSMSBackend(SMSOTPBackend):

    template_name = "drf_2fa/sms/message.txt"
    
    def get_twilio_client(self):
        try:
            client = Client(self.settings.TWILIO_ACCOUNT_SID, self.settings.TWILIO_AUTH_TOKEN)
        except Exception as e:
            raise SMSClientCouldNotCreate(e)
        return client
    
    def get_receiver_phone_number(self, user):
        try:
            return getattr(user, self.settings.PHONE_NUMBER_FIELD)
        except:
            raise InvalidPhoneNumberField

    def send_otp(self, user):
        client = self.get_twilio_client()
        receiver_phone_number = self.get_receiver_phone_number(user)
        message_body = self.get_message_content()
        try:
            client.messages.create(
                to=receiver_phone_number,
                from_=self.settings.TWILIO_NUMBER,
                body=message_body
            )
        except TwilioRestException as e:
            raise SMSCouldNotSend(e)
