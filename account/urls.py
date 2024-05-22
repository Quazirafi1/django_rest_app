from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView   
)

urlpatterns = [
    path('api/token/', csrf_exempt(TokenObtainPairView.as_view()), name='token_obtain_view'),
    path('api/token/refresh/', csrf_exempt(TokenRefreshView.as_view()), name='token_refresh_view'),
    
    path("login/", obtain_auth_token, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("test/", views.test_token, name="test"),
    path("register/", views.user_register, name="register"),    
]
