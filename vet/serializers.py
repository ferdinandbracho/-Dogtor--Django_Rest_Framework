from re import I
from django.db.models.fields import EmailField
from rest_framework import serializers

class PetOwnersContactListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length='255')

class PetOwnersListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)


class PetListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length='255')
    owner = PetOwnersContactListSerializer()