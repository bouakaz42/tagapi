from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 
from .views import BioList  , BioDetails

urlpatterns = [
    path('', BioList.as_view() , name='user-register'),
    path('<int:pk>', BioDetails.as_view() , name='user-login'),
]
