from django.urls import path
from .views import *


urlpatterns = [
    path('user/me/', UserInfo.as_view(), name="user_info"),
]
