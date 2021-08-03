# Django
from django.shortcuts import get_object_or_404

# Rest_Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Serializers
from .serializers import (
    # Pet Owner serializers
    PetOwnersListSerializer, 
    PetOwnerSeralizer, 
    PetOwnerUpdateSerializer,

    # Pet serializers
    PetListSerializer, 
    PetSerializer, 
    PetUpdateSerializer
    )

# Models 
from .models import PetOwner, Pet

class PetOwnersListCreateAPIView(APIView):
    """
    View to list all pet owners in the system
    """
    serializer_class = PetOwnersListSerializer

    def get(self, request):
        owner_queryset = PetOwner.objects.all()
        serializer = self.serializer_class(owner_queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PetOwnerSeralizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_instance = serializer.save()
        serialized_instance = PetOwnerSeralizer(created_instance)
        return Response(serialized_instance.data, status.HTTP_201_CREATED)

class PetOwnerDetailUpdateDeleteAPIView(APIView):
    """"
    View For Owner details
    """
    serializer_class = PetOwnerSeralizer

    def get(self, request, pk):
        # owner = PetOwner.objects.get(id=pk)
        owner = get_object_or_404(PetOwner, id=pk)
        serializer = self.serializer_class(owner)
        return Response(serializer.data)

    def patch(self, request, pk):
        owner = get_object_or_404(PetOwner, id=pk)
        serializer = PetOwnerUpdateSerializer(instance=owner, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_instance = serializer.save()
        serialezed_instance = self.serializer_class(updated_instance)
        return Response(serialezed_instance.data)

    def delete(self, request, pk):
        owner = get_object_or_404(PetOwner, id=pk)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PetListCreateAPIView(APIView):
    """
    View to list all pets in the system
    """
    serializer_class = PetListSerializer

    def get(self, request):
        pet_queryset = Pet.objects.all()
        serializer = self.serializer_class(pet_queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_instance = serializer.save()
        serialized_instance = PetSerializer(created_instance)
        return Response(serialized_instance.data, status.HTTP_201_CREATED)

class PetDetailUpdateDeleteAPIView(APIView):
    """
    View for Pet details
    """
    serializer_class = PetSerializer

    def get(self, request, pk):
        # pet = Pet.objects.get(id=pk)
        pet = get_object_or_404(Pet, id=pk)
        serializer = self.serializer_class(pet)
        return Response(serializer.data)

    def patch(self, request, pk):
        pet = get_object_or_404(Pet, id=pk)
        serializers = PetUpdateSerializer(instance=pet, data=request.data)
        serializers.is_valid(raise_exception=True)
        updated_instance = serializers.save()
        serialized_instance = self.serializer_class(updated_instance)
        return Response(serialized_instance.data)

    def delete(self, request, pk):
        pet = get_object_or_404(Pet, id=pk)
        pet.delete()
        return  Response(status.HTTP_204_NO_CONTENT)

