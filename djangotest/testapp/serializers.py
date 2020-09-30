from rest_framework import serializers
from .models import People
from django.contrib.auth.models import User


class ChangePasswordSerializer(serializers.Serializer):
    """
        Serializer for password change endpoint.
        """
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PeopleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ("name", "age")


class PeopleAdminListSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = "__all__"
