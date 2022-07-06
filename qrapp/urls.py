from django.urls import path
from .views import QrList  , QrDetails

urlpatterns = [
    path('', QrList.as_view() , name='qr-lists'),
    path('<int:pk>', QrDetails.as_view() , name='qr-deatails'),
]
