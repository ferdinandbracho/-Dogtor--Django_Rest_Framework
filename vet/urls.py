from django.urls import path

from .views import (
#   Pet Owner
    PetOwnerListCreateAPIView,
    PetOwnerRetriveUpdateDestroy,
    
#   Pet
    PetListCreateAPIView,
    PetRetriveUpdateDestroy,

    # Pet Date
    PetDateListAPIView,
    PetDateRetriveUpdateDestroy,

)
# Auth View
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    # Owner
    path('owners/',PetOwnerListCreateAPIView.as_view(), name='owner_list' ),
    path('owners/<int:pk>/',PetOwnerRetriveUpdateDestroy.as_view(), name='owner_list' ),

    # Pet
    path('pets/', PetListCreateAPIView.as_view(), name='pet_list'),
    path('pets/<int:pk>', PetRetriveUpdateDestroy.as_view(), name='pet_list'),

    # PetDate
    path('dates/', PetDateListAPIView.as_view(), name='date_list-create'),
    path('dates/<int:pk>', PetDateRetriveUpdateDestroy.as_view(), name='date_retrieve-update-destroy'),

    # Login 
    path('token-auth/', authtoken_views.obtain_auth_token, name='token_auth'),
]
