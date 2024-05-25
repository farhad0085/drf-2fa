from drf_2fa.backends import BaseMessageOTPBackend
from django.template.loader import render_to_string
from django.core.mail import send_mail
from drf_2fa.settings import drf_2fa_settings


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
