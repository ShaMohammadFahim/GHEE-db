from rest_framework import serializers
from .models import CustomUser, Role


class UserSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role_name = validated_data.pop('role_name', 'Customer')
        try:
            role_instance = Role.objects.get(name=role_name)
        except Role.DoesNotExist:
            role_instance = Role.objects.get(name='Customer')

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=role_instance 
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.name', read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone', 'address', 'role_name']