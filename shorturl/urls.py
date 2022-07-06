from django.urls import path
from .views import QrLinkList  , QrLinkDetails

urlpatterns = [
    path('', QrLinkList.as_view() , name='qrlink-lists'),
    path('<int:pk>', QrLinkDetails.as_view() , name='qrlink-details'),
]
