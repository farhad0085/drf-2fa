# Customization

## Customizing Login API

In your `views.py`, customize the behavior of the Login API as follows:

```python
from drf_2fa.views import LoginAPIView

class My2FALoginAPIView(LoginAPIView):
    serializer_class = MyLoginSerializer # Ensure the serializer includes username and password fields.

    def get_is_2fa_required(self, user):
        """
        Determine if 2FA is required for the user.
        Logic can be customized based on user attributes.
        """

        is_2fa_enabled = user.is_2fa_enabled

        return is_2fa_enabled

    def get_api_token(self, user):
        """
        Generate an API token and send it to the user.
        Token type (JWT/Token) may vary based on DRF configuration.
        Here, we're using token-based authentication.
        """
        token, _ = Token.objects.get_or_create(user=user)
        return token.key
```

## Customizing OTP Backend

### EmailOTPBackend
To customize the **email subject** and **email body**, simply override the following templates:

- `templates/drf_2fa/email/subject.txt` - customize email subject
- `templates/drf_2fa/email/message.html` - customize email body

### TwilioSMSBackend
For altering the **message content**, you can override the template located at:

- `templates/drf_2fa/sms/message.txt`

### AuthenticatorAppOTPBackend
The backend typically doesn't require further modification. However, if necessary, you can subclass the backend and override the `save_and_send_otp_code` method as follows:

```python
class MyAuthenticatorOTPBackend(AuthenticatorAppOTPBackend):
    def save_and_send_otp_code(self, user):
        """
        Override this method if you need custom behavior.
        It doesn't require any action by default, but you can add your own logic here if needed.
        """
        # do something with user
        pass
```

Refer to the [API Reference](./api_reference.md) for further details on customization options.