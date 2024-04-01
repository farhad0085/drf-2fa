from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class AuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        
        try:
            user = UserModel.objects.filter(email__iexact=username).first()
            if user.check_password(password):
                return user
        except:
            return None

