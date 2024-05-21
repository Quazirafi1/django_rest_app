from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("test/", views.test_token, name="test"),
    path("register/", views.user_register, name="register"),    
]
