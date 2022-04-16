from dataclasses import field
from enum import unique
from pyexpat import model
from django.contrib.auth.models import User
from importlib_metadata import requires

from rest_framework import serializers

import users

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(read_only=True)


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'email', 'password']