from django.urls import path
from api.views import ProfileAPI, EmailAPI

urlpatterns = [
    path('profile/', ProfileAPI.as_view(), name='profile'),
    path('email/', EmailAPI.as_view(), name='email'),
]
