from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class AuthSecret(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    secret = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField()

    def generate_auth_code(self):
        pass

