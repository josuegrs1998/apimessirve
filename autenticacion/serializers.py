from rest_framework import serializers
from django.contrib.auth import get_user_model
from productos.serializers import OrdenSerializer
from django.contrib.auth.hashers import make_password, check_password


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        # This makes the password to be a write only field, it cannot be read 
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        # Creates a User using the object model and passing the arguments that are validated
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    orden_set = OrdenSerializer(many=True)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'password', 'orden_set', 'groups']
        extra_kwargs = {'password': {'write_only': True}}

