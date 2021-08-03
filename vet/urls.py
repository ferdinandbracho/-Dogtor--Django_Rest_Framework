from django.urls import path

from .views import (
    PetOwnersListCreateAPIView, 
    PetListCreateAPIView, 
    PetOwnerDetailUpdateDeleteAPIView, 
    PetDetailUpdateDeleteAPIView
)

urlpatterns = [
    path('owners/', PetOwnersListCreateAPIView.as_view(), name='owners_retrive-create'),
    path('owners/<int:pk>/', PetOwnerDetailUpdateDeleteAPIView.as_view(), name='owner_retrive-update-delete' ),
    path('pets/', PetListCreateAPIView.as_view(), name='pets_retrive-create'),
    path('pets/<int:pk>/', PetDetailUpdateDeleteAPIView.as_view(), name='pet_retrive-update-delete'),
]
