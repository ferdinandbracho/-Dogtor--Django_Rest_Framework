from django.shortcuts import get_object_or_404

# Rest_Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

# Serializers
from .serializers import PetOwnersListSerializer, PetListSerializer, PetOwnerSeralizer, PetSerializer

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
        return Response(created_instance.__dict__)

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
        return Response(created_instance.__dict__)

class PetOwnerDetailAPIView(APIView):
    """"
    View For Owner details
    """
    serializer_class = PetOwnerSeralizer

    def get(self, request, pk):
        # owner = PetOwner.objects.get(id=pk)
        owner = get_object_or_404(PetOwner, id=pk)
        serializer = self.serializer_class(owner)
        return Response(serializer.data)

class PetDetailAPIView(APIView):
    """
    View for Pet details
    """
    serializer_class = PetSerializer

    def get(self, request, pk):
        # pet = Pet.objects.get(id=pk)
        pet = get_object_or_404(Pet, id=pk)
        serializer = self.serializer_class(pet)
        return Response(serializer.data)