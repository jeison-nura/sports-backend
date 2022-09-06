from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    first_name = serializers.CharField(min_length=4, max_length=128, required=True)
    last_name = serializers.CharField(min_length=4, max_length=128, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
       
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
