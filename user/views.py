from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import PasswordCheckSerializer

User = get_user_model()

# Create your views here.


class PasswordCheckViewSet(viewsets.ModelViewSet):
    serializer_class = PasswordCheckSerializer
    queryset = User.objects.all()

    @action(methods=['post'], detail=True)
    def password_check(self, request, pk=None):
        user = get_object_or_404(self.get_queryset(), pk=pk)
        if (request.data.get('password')):
            print(self)
            plain_pass = request.data.get('password')
            encoded_pass = user.password
            return Response(check_password(plain_pass, encoded_pass))
    #@action(methods=['patch'], detail=True)
    #def password_update(self, request, pk=None):
    #    user_to_update = get_object_or_404(self.get_queryset(), pk=pk)
    #    # Hash password but passwords are not required
    #    if ('password' in request.data):
    #        password = make_password(request.data.get('password'))
    #        user_to_update.password = password
    #        user_to_update.save()
    #        return Response('Password Updated Successfully!')
    #    else:
    #        user_to_update.save()
    #        return Response('There was an error updating the password')