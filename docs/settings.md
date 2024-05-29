# Settings

## OTP_BACKEND
Choose the OTP backend to use. For a list of supported OTP backends, please refer to the [API Reference](./backends.md)

> **_NOTE:_** Currently, only one OTP method per project is supported.


| Type      |      Default                              | Required                             |
|-----------|-------------------------------------------| ------------------------------------ |
| string    | `drf_2fa.backends.email.EmailOTPBackend`  | No                                   |


## TWILIO_ACCOUNT_SID
Your Twilio account SID. You can find this credential in your Twilio console.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| string    | `None`                                    |Yes, if `TwilioSMSBackend` is selected in `OTP_BACKEND`|

## TWILIO_AUTH_TOKEN
Your Twilio auth token. You can find this credential in your Twilio console.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| string    | `None`                                    |Yes, if `TwilioSMSBackend` is selected in `OTP_BACKEND`|

## TWILIO_NUMBER
Your Twilio phone number. You can find this credential in your Twilio console. This phone number will be used as the SMS sender.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| string    | `None`                                    |Yes, if `TwilioSMSBackend` is selected in `OTP_BACKEND`|

## PHONE_NUMBER_FIELD
The field in the User model that contains the user's phone number. If the phone number is saved in any other model, ignore this setting. Simply subclass `TwilioSMSBackend` and override the `get_receiver_phone_number` method. The phone number returned from this method will receive the OTP SMS.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| string    | `phone_number`                            |Yes, if `TwilioSMSBackend` is selected in `OTP_BACKEND`|

## OTP_LENGTH
The length of OTP, used only if you are using an email/SMS OTP backend.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| integer   | 6                                         | No                                                    |

## OTP_EXPIRE
Defines after how long the OTP will expire. Used only if you are using an email/SMS OTP backend.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| timedelta | `datetime.timedelta(seconds=86400)`       | No                                                    |

## OTP_EMAIL_FROM
For an email OTP backend, specify the sender's email. Used only in email OTP backends.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| string    | `settings.DEFAULT_FROM_EMAIL`             | No                                                    |

## SHOW_OTP_MODEL_ADMIN
Set to True if you want to see `drf_2fa` model's admins in your admin site.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| boolean   | `False`                                   | No                                                    |

## QR_ISSUER_NAME
The QR issuer name, used in third-party authenticator apps to display the site name. Specify this setting to match it with your app name.

| Type      |      Default                              | Required                                              |
| --------- | ----------------------------------------- | ----------------------------------------------------- |
| string    | `DRF 2FA`                                 | Yes                                                   |
