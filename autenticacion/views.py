from django.shortcuts import render
from rest_framework.generics import GenericAPIView , ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import LoginSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from django.views import generic
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
import jwt

User = get_user_model()

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class ListaUsuario(ListCreateAPIView):
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return User.objects.all()
    
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'first_name', 'email')

class DetalleUsuario(RetrieveUpdateDestroyAPIView): #Para buscar 1 editar 1
    serializer_class = UserSerializer
    lookup_field='id'

    def get_queryset(self):
        return User.objects.all()

class RegisterView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if user:
            auth_token= jwt.encode({
                'id':user.id,
                'email':user.email,
                'direccion':user.direccion,
                'telefono':user.telefono,
                'first_name':user.first_name,
                'last_name': user.last_name
            }, settings.JWT_SECRET_KEY)

            serializer = LoginSerializer(user)

            data = {
                'user': serializer.data,'token':auth_token
            }
            return Response(data, status=status.HTTP_200_OK)

            #enviar respuesta
        return Response({'detail':'Credenciales invalidas'}, status=status.HTTP_401_UNAUTHORIZED)