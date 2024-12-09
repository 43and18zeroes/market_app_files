from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from user_auth_app.models import UserProfile
from .serializers import UserProfileSerializer, RegistrationSerializer

class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class CustomLoginView(ObtainAuthToken):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serilalizer = self.serializer_class(data=request.data)
        
        data = {}
        if serilalizer.is_valid():
            user = serilalizer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'username': user.username,
                'email': user.email,
            }
        else:
            data=serilalizer.errors
            
        return Response(data)
    
class RegistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serilalizer = RegistrationSerializer(data=request.data)
        
        data = {}
        if serilalizer.is_valid():
            saved_account = serilalizer.save()
            token, created = Token.objects.get_or_create(user=saved_account)
            data = {
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email,
            }
        else:
            data=serilalizer.errors
            
        return Response(data)