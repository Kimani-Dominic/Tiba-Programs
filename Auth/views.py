from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .models import *
from .serializers import *

# Create your views here.
class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({"message": "User registered successfully!"}, status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user_id": user.id,
                "username": user.username
            }, status.HTTP_200_OK )
            
        print(serializer.errors)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class UserSearch(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        query = request.GET.get('query', '')
        user = User.objects.filter(
            first_name__icontains=query) | User.objects.filter(last_name__icontains=query) | User.objects.filter(email__icontains=query)
        user_data = [{'id': user.id, 'name': str(user)} for user in user]
        return Response(user_data)