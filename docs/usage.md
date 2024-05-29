# Usage
To integrate Two-Factor Authentication (2FA) into your Django project using DRF_2FA, follow these simple steps:

1. Add URL Pattern:

Incorporate the drf_2fa URLs into your Django project's urlpatterns:

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
Based on `is_2fa_required` client will redirect user to 2FA code entry page.

Depending on the is_2fa_required flag, redirect the client to the 2FA code entry page.
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
