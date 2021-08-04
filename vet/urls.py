from django.urls import path
from rest_framework.fields import DateField

from .views import (
#   Pet Owner
#   PetOwnersListCreateAPIView, 
#   PetOwnerDetailUpdateDeleteAPIView, 
#   PetOwnerListGenericView,
#   PetOwnerRetriveApiView,
    PetOwnerListCreateAPIView,
    PetOwnerRetriveUpdateDestroy,
    
#   Pet
#   PetListCreateAPIView, 
#   PetDetailUpdateDeleteAPIView
#   PetListGenericView,
    PetListCreateAPIView,
    PetRetriveUpdateDestroy,

    # Pet Date
    PetDateListAPIView,
    PetDateRetriveUpdateDestroy
)

urlpatterns = [
    # Owner
    # path('owners/', PetOwnersListCreateAPIView.as_view(), name='owners_retrive-create'),
    # path('owners/<int:pk>/', PetOwnerDetailUpdateDeleteAPIView.as_view(), name='owner_retrive-update-delete' ),
    path('owners/',PetOwnerListCreateAPIView.as_view(), name='owner_list' ),
    path('owners/<int:pk>/',PetOwnerRetriveUpdateDestroy.as_view(), name='owner_list' ),
    # path('owners/<int:pk>/', PetOwnerRetriveApiView.as_view(), name='owner_retrive'),

    # Pet
    # path('pets/', PetListCreateAPIView.as_view(), name='pets_retrive-create'),
    # path('pets/<int:pk>/', PetDetailUpdateDeleteAPIView.as_view(), name='pet_retrive-update-delete'),
    path('pets/', PetListCreateAPIView.as_view(), name='pet_list'),
    path('pets/<int:pk>', PetRetriveUpdateDestroy.as_view(), name='pet_list'),

    # PetDate
    path('petdates/', PetDateListAPIView.as_view(), name='petdate_list-create'),
    path('petdates/<int:pk>', PetDateRetriveUpdateDestroy.as_view(), name='petdate_retrieve-update-destroy'),

]
