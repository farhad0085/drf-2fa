class BaseOTPBackend:

    def verify_otp(self, user, otp):
        pass
    
    def generate_otp(self, user):
        pass


class EmailOTPBackend(BaseOTPBackend):

    def send_otp():
        pass
