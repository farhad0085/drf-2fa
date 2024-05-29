from drf_2fa.backends import BaseMessageOTPBackend
from django.template.loader import render_to_string
from django.core.mail import send_mail


class EmailOTPBackend(BaseMessageOTPBackend):
    """
    OTP backend that sends OTP codes to users via email.

    Uses a template to generate the email message.

    Attributes:
        template_name (str): The name of the template file used to generate the email message.
    """

    template_name = "drf_2fa/email/message.html"

    def get_context_data(self):
        """
        Get the context data for rendering the email message template.

        Returns:
            dict (dict): Context data for rendering the email message template.
        """
        return {'otp_code': self.otp_code}

    def send_otp(self, user):
        """
        Send the OTP code to the user's email address.

        Args:
            user (User): The user object whose email address will receive the OTP code.
        """
        subject = render_to_string('drf_2fa/email/subject.txt')
        email_content = self.get_message_content()

        send_mail(
            subject=subject,
            message=email_content,
            from_email=self.settings.OTP_EMAIL_FROM,
            recipient_list=[user.email]
        )
