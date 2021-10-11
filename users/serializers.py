from .models import User

from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework_simplejwt.serializers import PasswordField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = PasswordField()
    TYPE_CHOICES = [
        ("ADMIN", "Administrator"),
        ("SALE", "Sales contact"),
        ("SUPPORT", "Support contact"),
    ]
    role = serializers.ChoiceField(choices=TYPE_CHOICES, default="SUPPPORT")

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "role",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, password):
        if validate_password(password) is None:
            return make_password(password)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
