# app/urls.py

from django.urls import path

from app.views import UserRegistrationView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]
