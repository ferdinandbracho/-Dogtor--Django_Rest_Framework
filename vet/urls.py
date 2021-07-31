from django.urls import path

from .views import PetOwnersList, PetList

urlpatterns = [
    path('owners/', PetOwnersList.as_view(), name='owners_list'),
    path('pets/', PetList.as_view(), name='pets_lsit'),
]
