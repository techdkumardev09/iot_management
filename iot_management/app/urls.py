# app/urls.py

from django.urls import path, include
from rest_framework import routers
from app.views import DeviceViewSet, UserRegistrationView

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('', include(router.urls)),
]
