from django.shortcuts import render

# Rest_Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

# Serializers
from .serializers import PetOwnersListSerializer, PetListSerializer

# Models 
from .models import PetOwner, Pet


class PetOwnersList(APIView):
    """
    View to list all pet owners in the system
    """

    serializer_class = PetOwnersListSerializer

    def get(self, request):
        # owners = [
        #     {'id': owner.id, 'first_name': owner.first_name} 
        #     for owner in PetOwner.objects.all()
        # ]
        # return Response(owners)

        owner_queryset = PetOwner.objects.all()
        serializer = self.serializer_class(owner_queryset, many=True)
        return Response(serializer.data)

class PetList(APIView):
    """
    View to list all pets in the system
    """

    serializer_class = PetListSerializer

    def get(self, request):
        # pets = [
        #     {'id': pet.id, 'name': pet.name, 'type': pet.type}
        #     for pet in Pet.objects.all()
        # ]
        # return Response(pets)

        pet_queryset = Pet.objects.all()
        serializer = self.serializer_class(pet_queryset, many=True)
        return Response(serializer.data)