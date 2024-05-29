# Configuration

In your django `settings` module, add following settings.

```python
DRF_2FA_SETTINGS = {
    "OTP_BACKEND": "drf_2fa.backends.authenticator.AuthenticatorAppOTPBackend",
    ... # Other settings
}
```

For full settings options, please refer to [Settings](./settings.md)
