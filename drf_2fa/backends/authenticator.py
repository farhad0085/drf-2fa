import hmac, base64, struct, hashlib, time
from drf_2fa.backends import BaseOTPBackend
from drf_2fa.models import AuthSecret


class AuthenticatorAppOTPBackend(BaseOTPBackend):

    def get_hotp_token(self, secret, intervals_no):
        """Function taken from https://medium.com/analytics-vidhya/understanding-totp-in-python-bbe994606087"""
        key = base64.b32decode(secret, True)
        # decoding the key
        msg = struct.pack(">Q", intervals_no)
        # conversions between Python values and C structs represente
        h = hmac.new(key, msg, hashlib.sha1).digest()
        o = o = h[19] & 15
        # Generate a hash using both of these. Hashing algorithm is HMAC
        h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
        # unpacking
        return h
    
    def get_totp_token(self, secret):
        # ensuring to give the same otp for 30 seconds
        x = str(self.get_hotp_token(secret, intervals_no=int(time.time())//30))
        # adding 0 in the beginning till OTP has 6 digits
        while len(x) != 6:
            x+='0'
        return x

    def verify_otp(self, user, otp):
        obj = AuthSecret.objects.filter(user=user).first()
        if not obj:
            return False
        return self.get_totp_token(obj.secret) == otp

    def save_and_send_otp_code(self, user):
        pass # since it's a authenticator app, no need to send otp to user
    
