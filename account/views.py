
# Create your views here.
from rest_framework.decorators import api_view  , permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
from .serializers import RgisterSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.renderers import  JSONRenderer

class CustomAuthToken(ObtainAuthToken):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
       # login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })



# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def RegisterView(request):
    if request.method == 'POST':
     serializer = RgisterSerializer(data=request.data)
    if serializer.is_valid():
        ss = serializer.save()
        token = Token.objects.get(user=ss).key
        data = { 'data': serializer.data , 'token':token}
        return Response(data , status=201)
    return Response(serializer.errors , status=400)    
    