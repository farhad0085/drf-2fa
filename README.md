# Supports
1. Email
2. SMS
2. Authenticator App


1. Login api
    - ask for auth code if correct user/pass
    - otherwise fails
    - ability to skip/disable 2fa on current device


# Workflow
1. Login
    - send username/password
    - returns an id (store in db) and save an OTP
    - user enter OTP, send request with the id received in the previous step and OTP
    - verify : check the id and match OTP (based on OTPBackend, can be self/authenticator app)
    - final returns token (based on authentication_backend)
