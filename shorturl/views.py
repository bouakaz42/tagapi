
# Create your views here.
from .models import Shorturl
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 
from rest_framework.renderers import JSONRenderer
from .serializers import ShorturlSerializer



class QrLinkList(generics.ListCreateAPIView):
    queryset = Shorturl.objects.all()
    serializer_class = ShorturlSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    def get_queryset(self):
        return Shorturl.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class QrLinkDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shorturl.objects.all()
    serializer_class = ShorturlSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    def get_queryset(self):
        return Shorturl.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    def perform_destroy(self, instance):
        instance.delete()

