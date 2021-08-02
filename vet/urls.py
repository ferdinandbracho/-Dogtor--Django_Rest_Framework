from django.urls import path

from .views import PetOwnersListCreateAPIView, PetListCreateAPIView, PetOwnerDetailAPIView, PetDetailAPIView

urlpatterns = [
    path('owners/', PetOwnersListCreateAPIView.as_view(), name='owners_list'),
    path('owners/<int:pk>/', PetOwnerDetailAPIView.as_view(), name='owner_detail' ),
    path('pets/', PetListCreateAPIView.as_view(), name='pets_lsit'),
    path('pets/<int:pk>/', PetDetailAPIView.as_view(), name='pet_detail'),
]
