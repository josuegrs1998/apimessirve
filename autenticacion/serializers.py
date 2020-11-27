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
        enc_pass = make_password(password, salt=None, hasher='default')
        user.set_password(enc_pass)
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    orden_set = OrdenSerializer(many=True)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'password', 'orden_set']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, attrs):
        if User.objects.filter(email = attrs['email']).exists():
            raise serializers.ValidationError({'email', ('El email ya esta en uso')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    


