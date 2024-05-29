# Configuration

To set up `DRF 2FA` in your Django project, add the following settings to your settings.py module:

```python
DRF_2FA_SETTINGS = {
    "OTP_BACKEND": "drf_2fa.backends.authenticator.AuthenticatorAppOTPBackend",
    ... # Other settings
}
```

For a comprehensive list of all available settings options, please refer to the [Settings Documentation](./settings.md)
