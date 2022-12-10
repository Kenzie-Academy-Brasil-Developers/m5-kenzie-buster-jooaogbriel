from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=127)
    password = serializers.CharField(max_length=127, write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField(read_only=True)
    is_employee = serializers.BooleanField(default=False,allow_null=True,)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        is_employe = validated_data.pop("is_employee")

        if is_employe:
            sup_user = User.objects.create_superuser(**validated_data, is_employee=True)
            return sup_user 
        sup_user= User.objects.create_user(**validated_data, is_employee=False)
        return sup_user


    def validate_username(self,username):
        very_username = User.objects.filter(username = username).exists()

        if very_username:
            raise serializers.ValidationError(detail="username already taken.")
        return username


    def validate_email(self, email):
        verify_email = User.objects.filter(email = email).exists()
        if verify_email:
            raise serializers.ValidationError(detail= "email already registered.")
        return email


class JWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser

        return token