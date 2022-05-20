from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Messages


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","password"]

    def validate(self, attrs):
        email = attrs.get("email")
        if not email:
            raise serializers.ValidationError("Email is required!")
        return attrs


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "password"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]



class MessageSerializer(serializers.ModelSerializer):
    created_by=serializers.SerializerMethodField("getUser")
    class Meta:
        model = Messages
        fields = ["id","message","created_at","updated_at","user","created_by"]

    def getUser(self,object):
        print(object,"<---- This object ")
        user=User.objects.get(username=object.user)
        serializer=UserSerializer(user)
        return serializer.data

