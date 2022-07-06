from django.shortcuts import get_object_or_404, render
from .models import Bio
from .serializers import BioSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view  , permission_classes
from rest_framework.response import Response
from .serializers import ContentSerializer , SociallinksSerializer
class BioList(generics.ListCreateAPIView):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    def get_queryset(self):
        return Bio.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class BioDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = (JSONRenderer,)
    def get_queryset(self):
        return Bio.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    def perform_destroy(self, instance):
        instance.delete()
# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def biolink(request , page_alias):
    if request.method == 'GET':
        final_page = get_object_or_404(Bio, page_alias=page_alias)
        content = ContentSerializer(final_page.content)
        social_links = SociallinksSerializer(final_page.social_links)
        
        final_data = {'name': final_page.page_name,  'page_alias': final_page.page_alias ,'content': content.data , 'social_links': social_links.data}
        return Response(final_data , status=201)
    return Response(data={"error":"something wrong"} , status=400)    