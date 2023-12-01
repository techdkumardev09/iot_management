# app/urls.py

from django.urls import path, include
from rest_framework import routers
from app.views import DeviceViewSet, TelemetryDataViewSet, UserRegistrationView

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'telemetry', TelemetryDataViewSet)


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('', include(router.urls)),
]
