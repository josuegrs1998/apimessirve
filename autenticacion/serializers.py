from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name' ,'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50,min_length=2)
    username = serializers.CharField(max_length=100, min_length=4)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password']
    
    def validate(self, attrs):
        if User.objects.filter(username = attrs['username']).exists():
            raise serializers.ValidationError({'username', ('El username ya esta en uso')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    


