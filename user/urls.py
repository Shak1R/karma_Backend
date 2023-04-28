from django.urls import path
from user.views import login, registration

urlpatterns = [
    path('login/', login),  # ../user/login
    path('registration/', registration),  # ../user/registration
]