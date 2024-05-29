from twilio.rest import Client
from drf_2fa.backends import SMSOTPBackend
from twilio.base.exceptions import TwilioRestException
from drf_2fa.exceptions import InvalidPhoneNumberField, SMSClientCouldNotCreate, SMSCouldNotSend


class TwilioSMSBackend(SMSOTPBackend):
    """
    OTP backend that sends OTP codes to users via Twilio SMS.

    Uses the Twilio API to send SMS messages containing OTP codes.

    Attributes:
        template_name (str): The name of the template file used to generate the SMS message.
    """

    template_name = "drf_2fa/sms/message.txt"
    
    def get_twilio_client(self):
        """
        Get the Twilio client object.

        Returns:
            Client (Client): The Twilio client object for sending SMS messages.
        
        Raises:
            SMSClientCouldNotCreate: If the Twilio client object could not be created.
        """
        try:
            client = Client(self.settings.TWILIO_ACCOUNT_SID, self.settings.TWILIO_AUTH_TOKEN)
        except Exception as e:
            raise SMSClientCouldNotCreate(e)
        return client
    
    def get_receiver_phone_number(self, user):
        """
        Get the phone number of the user to receive the OTP SMS.

        Args:
            user (User): The user object for whom the OTP SMS is intended.

        Returns:
            str (str): The phone number of the user.

        Raises:
            InvalidPhoneNumberField: If the user's phone number field is invalid or missing.
        """
        
        try:
            return getattr(user, self.settings.PHONE_NUMBER_FIELD)
        except:
            raise InvalidPhoneNumberField

    def send_otp(self, user):
        """
        Send the OTP code to the user's phone number via Twilio SMS.

        Args:
            user (User): The user object whose phone number will receive the OTP SMS.
        
        Raises:
            SMSCouldNotSend: If the OTP SMS could not be sent to the user's phone number.
        """

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
