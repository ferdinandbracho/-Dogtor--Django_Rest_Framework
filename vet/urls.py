from django.urls import path

from .views import (
    # Pet Owner
#   PetOwnersListCreateAPIView, 
#   PetOwnerDetailUpdateDeleteAPIView, 
    PetOwnerListGenericView,
    PetOwnerRetriveApiView,
    
    # Pet
#   PetListCreateAPIView, 
#   PetDetailUpdateDeleteAPIView
    PetListGenericView,
)

urlpatterns = [
    # Owner
    # path('owners/', PetOwnersListCreateAPIView.as_view(), name='owners_retrive-create'),
    # path('owners/<int:pk>/', PetOwnerDetailUpdateDeleteAPIView.as_view(), name='owner_retrive-update-delete' ),
    path('owners/',PetOwnerListGenericView.as_view(), name='owner_list' ),
    path('owners/<int:pk>/', PetOwnerRetriveApiView.as_view(), name='owner_retrive'),

    # Pet
    # path('pets/', PetListCreateAPIView.as_view(), name='pets_retrive-create'),
    # path('pets/<int:pk>/', PetDetailUpdateDeleteAPIView.as_view(), name='pet_retrive-update-delete'),
    path('pets/', PetListGenericView.as_view(), name='pet_list'),
]
