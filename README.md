# DRF 2FA (Two Factor Authentication)
Integrate 2 Factor Authentication in Your Django REST API project easily.

## Features
- Email based OTP authentication (Added)
- SMS based OTP authentication (Added)
    - Twilio (Added)
- Third party Authenticator App authentication (Added)
- Ability to skip/disable 2fa on current device (PENDING)
- Ability to have multiple authentication method (PENDING)

## Installation

1. Install the package
    ```sh
    pip install drf_2fa
    ```

2. Add `drf_2fa` to `INSTALLED_APPS`
    ```python
    INSTALLED_APPS = [
        ...
        'drf_2fa',
        ...
    ]
    ```

3. Tweak settings
    ```python
    DRF_2FA_SETTINGS = {
        "OTP_BACKEND": "drf_2fa.backends.email.EmailOTPBackend",
        "OTP_LENGTH": 6,
        "OTP_EXPIRE": datetime.timedelta(seconds=86400),
        "OTP_EMAIL_FROM": "noreply@gmail.com",
        ... # other settings
    }
    ```
    > For full settings, please refer to the documentation.

4. Migrate database changes:
    ```
    python manage.py migrate
    ```
