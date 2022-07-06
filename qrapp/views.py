
# Create your views here.
from .models import Qrcode
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import QrcodeSerializer



class QrList(generics.ListCreateAPIView):
    queryset = Qrcode.objects.all()
    serializer_class = QrcodeSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    def get_queryset(self):
        return Qrcode.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class QrDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Qrcode.objects.all()
    serializer_class = Qrcode
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    def get_queryset(self):
        return Qrcode.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    def perform_destroy(self, instance):
        instance.delete()

