
# Rest_Framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import (
    # Pet Owner serializers
    PetOwnerListSerializerModel,
    PetOwnerModelSerializer,

    # Pet serializers
    PetListModelSerializer,
    PetModelSerializer,

    # PetDate
    PetDateModelSerializer,
    PetDatePetListModelSerializer,
    PetDatePartialUpdateModelSerializer,

    )

# Models 
from .models import PetOwner, Pet, PetDate

# !Pet Owner Views 
class PetOwnerListCreateAPIView(generics.ListCreateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerListSerializerModel
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name']
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'POST':
            serializer_class = PetOwnerModelSerializer
        return serializer_class

class PetOwnerRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerModelSerializer

# !Pet Views
class PetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'POST':
            serializer_class = PetModelSerializer
        return serializer_class

class PetRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetModelSerializer

# !Dates Views 
class PetDateListAPIView(generics.ListCreateAPIView):
    queryset = PetDate.objects.all()
    serializer_class = PetDateModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['pet__owner__first_name', 'pet__name']

    def get_queryset(self):
        pet_id = self.request.GET.get('pet')
        owner_id = self.request.GET.get('owner')
        filters = {}
        if pet_id:
            filters['pet__id'] = pet_id
        if owner_id:
            filters['pet__owner__id'] = owner_id
        return self.queryset.filter(**filters)


class PetDateRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    queryset = PetDate.objects.all()
    serializer_class = PetDatePetListModelSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'PATCH':
            serializer_class = PetDatePartialUpdateModelSerializer
        return serializer_class
