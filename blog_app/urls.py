from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet, basename="blogs")

urlpatterns = [
    path('', include(router.urls))
]
