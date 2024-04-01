from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import UserManager


class UserAccount(AbstractUser):
    """Custom user model for our system"""

    username = None
    email = models.EmailField('Email address', unique=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
