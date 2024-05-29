# Settings

## OTP_BACKEND
OTP Backend to use, for list of supported OTP backend, please refer to [API Reference](./backends.md)

> **_NOTE:_** currently we support one otp method per project

| Type      |      Default                              | Required                             |
|-----------|-------------------------------------------| ------------------------------------ |
| string    | `drf_2fa.backends.email.EmailOTPBackend`  | No                                   |


## TWILIO_ACCOUNT_SID
Your Twilio account SID, You can get this credentials in your twilio console.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| string    | `None`                                    |Yes, if `TwilioSMSBackend` is selected in `OTP_BACKEND`|

## TWILIO_AUTH_TOKEN
Your Twilio auth token, You can get this credentials in your twilio console.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| string    | `None`                                    |Yes, if `TwilioSMSBackend` is selected in `OTP_BACKEND`|

## TWILIO_NUMBER
Your Twilio phone number, You can get this credentials in your twilio console. This phone number will be used for sms sender.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| string    | `None`                                    |Yes, if `TwilioSMSBackend` is selected in `OTP_BACKEND`|

## PHONE_NUMBER_FIELD
The field in `User` model which contains user's phone number. If you've phone number saved in any other model,
ignore this settings. Simply subclass `TwilioSMSBackend`, and override `get_receiver_phone_number` method.
Phone number returned from this method will receive OTP sms

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| string    | `phone_number`                            |Yes, if `TwilioSMSBackend` is selected in `OTP_BACKEND`|

## OTP_LENGTH
Length of OTP, used only if you use an email/sms otp backend.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| integer   | 6                                         | No                                                    |

## OTP_EXPIRE
Define after how long, the OTP will be expired. Used only if you use an email/sms otp backend.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| timedelta | `datetime.timedelta(seconds=86400)`       | No                                                    |

## OTP_EMAIL_FROM
For an email otp backend, specify the sender email. Used only in email otp backends.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| string    | `settings.DEFAULT_FROM_EMAIL`             | No                                                    |

## SHOW_OTP_MODEL_ADMIN
Set to True if you want to see `drf_2fa` model's admins in your admin site.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| boolean   | `False`                                   | No                                                    |

## QR_ISSUER_NAME
QR issuer name, used in third party authenticator app, for displaying the site name. Specify this setting to match it with your app name.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| string    | `DRF 2FA`                                 | Yes                                                   |
