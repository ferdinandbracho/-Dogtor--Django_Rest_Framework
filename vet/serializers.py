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
    type = serializers.ChoiceField(choices=Pet.PET_TYPES)
    owner_id = serializers.IntegerField()

    def create(self, validate_data):
        return Pet.objects.create(**validate_data)

class PetOwnerUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255, required=False)
    last_name = serializers.CharField(max_length=255, required=False)
    address = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance

class PetUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=False)
    type = serializers.CharField(max_length=255, required=False)
    owner_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        return instance