from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 
from .views import RegisterView  , CustomAuthToken

urlpatterns = [
    path('register', RegisterView , name='user-register'),
    path('login', CustomAuthToken.as_view() , name='user-login'),
]
