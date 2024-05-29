import hmac, base64, struct, hashlib, time
from drf_2fa.backends import BaseOTPBackend
from drf_2fa.models import AuthSecret


class AuthenticatorAppOTPBackend(BaseOTPBackend):
    """
    OTP backend that generates and verifies OTP tokens compatible with Authenticator apps.

    This backend implements the TOTP (Time-based One-Time Password) algorithm for generating
    OTP tokens, which are commonly used with Authenticator apps like Google Authenticator.
    """

    def get_hotp_token(self, secret, intervals_no):
        """
        Generate a HOTP (HMAC-based One-Time Password) token.

        Args:
            secret (str): The secret key used for generating the token.
            intervals_no (int): The number of time intervals since the epoch for which to generate the token.

        Returns:
            int (int): The HOTP token.

        Function taken from https://medium.com/analytics-vidhya/understanding-totp-in-python-bbe994606087
        """
        
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
        """
        Generate a TOTP (Time-based One-Time Password) token.

        Args:
            secret (str): The secret key used for generating the token.

        Returns:
            str (str): The TOTP token.
        """
        # ensuring to give the same otp for 30 seconds
        x = str(self.get_hotp_token(secret, intervals_no=int(time.time())//30))
        # adding 0 in the beginning till OTP has 6 digits
        while len(x) != 6:
            x+='0'
        return x

    def verify_otp(self, user, otp):
        """
        Verify an OTP token against the stored secret key for the user.

        Args:
            user (User): The user object whose OTP token is to be verified.
            otp (str): The OTP token to be verified.

        Returns:
            bool (bool): True if the OTP token is valid, False otherwise.
        """
        obj = AuthSecret.objects.filter(user=user).first()
        if not obj:
            return False
        return self.get_totp_token(obj.secret) == otp

    def save_and_send_otp_code(self, user):
        """
        No action needed for saving or sending OTP code for Authenticator apps.

        This method is empty as Authenticator apps handle OTP generation and entry without
        the need for saving or sending OTP codes.

        Args:
            user (User): The user object for whom the OTP code would be generated.
        """
        pass
    
