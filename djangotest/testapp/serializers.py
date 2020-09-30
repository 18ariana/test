from rest_framework import serializers
from .models import People


class PeopleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ("name", "age")


class PeopleAdminListSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = "__all__"
