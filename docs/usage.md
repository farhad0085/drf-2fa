# Usage
To integrate Two-Factor Authentication (2FA) into your Django project using DRF_2FA, follow these simple steps:

## Message Based 2FA
**Applicable for `EmailOTPBackend`, `TwilioSMSBackend` or any Messaged based 2FA**

1. Add URL Pattern:

Incorporate the `drf_2fa` URLs into your Django project's urlpatterns:

```python
from django.urls import path, include

urlpatterns = [
    ...,
    path('api/2fa/', include("drf_2fa.urls")),
    ...,
]
```

2. Initiate Login:

Make a POST request to the login endpoint:

`POST http://localhost:8000/api/2fa/login/`

Request Body:
```json
{
	"username": "charlesdarwin",
	"password": "supersecret"
}
```
Upon successful request, you'll receive a JSON response indicating the need for 2FA authentication along with the user ID:
Response:
```json
{
    "message": "2FA authentication is required",
    "user_id": 1,
    "is_2fa_required": true
}
```

Depending on the `is_2fa_required` flag, redirect the client to the 2FA code entry page.
Simultaneously, if configured, the system will trigger an OTP via Email/SMS.

3. Verify the OTP:

After receiving the OTP, send a POST request to the verification endpoint:

`POST http://localhost:8000/api/2fa/verify-otp/`

Request body:
```json
{
    "user_id": 1, // retrieved from previous step
    "otp_code": "793845" // received either through Email/SMS/Authenticator App
}
```

Upon successful verification, you'll receive a response confirming the authentication:

Response:
```json
{
    "message": "OTP Verified Successfully!",
    "status": "SUCCESS",
    "api_token": "c58b1f6609bd297a05ccf4574dfa712ae7e9f906"
}
```

The `api_token` provided here is basically the API key that you'd obtain from the direct login flow.

4. Done

You're all set! The authentication process is complete, and the user can now proceed with the authenticated session.

## Authenticator App Based 2FA

This guide explains how to set up `drf_2fa` for authenticator app, such as **Google Authenticator** or **Authy** etc.

**Applicable for `AuthenticatorAppOTPBackend` or any third party authenticator app based 2FA**

1. Configuration:

Set up the `OTP_BACKEND` to `AuthenticatorAppOTPBackend` in your Django `settings.py` module.
```python
DRF_2FA_SETTINGS = {
    "OTP_BACKEND": "drf_2fa.backends.authenticator.AuthenticatorAppOTPBackend",
}
```

2. Obtaining Authentication Secret:

Use the following endpoint to get the authentication secret required for setting up the authenticator app:

`GET http://localhost:8000/api/2fa/get-auth-secret/`

Response:
```json
{
    "name": "charlesdarwin@monkey.com",
    "issuer_name": "DRF 2FA",
    "auth_secret": "BCJFUO6L6YSWAFI2O2YECVI37VRFQWYR",
    "qr_code": "<svg width=\"49mm\" height=\"49mm\" version=\"1.1\" viewBox=\"0 0 49 49\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M4,4H5V5H4zM5,4H6V5H5zM6,4H7V5H6zM7,4H8V5H7zM8,4H9V5H8zM9...\" id=\"qr-path\" fill=\"#000000\" fill-opacity=\"1\" fill-rule=\"nonzero\" stroke=\"none\" /></svg>"
}
```

> **_NOTE:_** The client should display the **QR code** or the **auth secret** for the user to scan or enter into their authenticator app.

3. User Interface for Setup:

Below is an example React component to facilitate the setup process:

```jsx
import React, { useState, useEffect } from 'react';

const SetupAuthenticator = ({ history }) => {

  const [authSecretData, setAuthSecretData] = useState({})

  useEffect(() => {
    getAuthSecret().then(res => {
      setAuthSecretData(res.data)
    })
  }, []);

  return (
    <div className={classes.wrapper}>
      <div className={classes.content}>
        <h3>OTP Secret:</h3>
        <p><strong>{authSecretData.auth_secret}</strong></p>
        <p>Enter it inside a 2FA app (Google Authenticator, Authy) or scan the QR code below.</p>
        <img src={`data:image/svg+xml;utf8,${encodeURIComponent(authSecretData.qr_code)}`} alt="SVG" />
      </div>
    </div>
  );
}

export default SetupAuthenticator
```

4. Completing Setup:

After scanning the QR code with the authenticator app, the user will have the OTP code generated within the app for authentication. This code will be required during the login process. For login process please refer to [Message Based 2FA](#message-based-2fa)