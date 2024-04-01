from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginView.as_view(), name="login_url"),
    path('user/me/', UserInfo.as_view(), name="user_info"),
]
