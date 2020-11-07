from rest_framework import serializers
from django.contrib.auth.models import User

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

    


