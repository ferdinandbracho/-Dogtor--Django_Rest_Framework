from rest_framework import serializers
from .models import PetOwner, Pet

# class PetOwnersContactListSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     first_name = serializers.CharField(max_length=255)
#     last_name = serializers.CharField(max_length=255)
#     email = serializers.EmailField()
#     phone = serializers.CharField(max_length='255')

class PetOwnersListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

class PetListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length='255')
    # owner = PetOwnersContactListSerializer()

class PetOwnerSeralizer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    address = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()

    def create(self, validate_data):
        return PetOwner.objects.create(**validate_data)

class PetSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    type = serializers.CharField()
    owner = serializers.CharField()

    def create(self, validate_data):
        return Pet.objects.create(**validate_data)
