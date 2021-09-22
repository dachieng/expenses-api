from django.urls import path
from authentication.views import UserRegistration

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register')
]
