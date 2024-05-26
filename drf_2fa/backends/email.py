from drf_2fa.backends import BaseMessageOTPBackend
from django.template.loader import render_to_string
from django.core.mail import send_mail


class EmailOTPBackend(BaseMessageOTPBackend):
    """Send OTP in user's email"""

    template_name = "drf_2fa/email/message.html"

    def get_context_data(self):
        return {'otp_code': self.otp_code}

    def send_otp(self, user):
        subject = render_to_string('drf_2fa/email/subject.txt')
        email_content = self.get_message_content()

        send_mail(
            subject=subject,
            message=email_content,
            from_email=self.settings.OTP_EMAIL_FROM,
            recipient_list=[user.email]
        )
