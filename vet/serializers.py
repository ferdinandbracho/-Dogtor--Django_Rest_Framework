from rest_framework import serializers
from .models import PetOwner, Pet, PetDate

# ?Pet owner serializers
class PetOwnerListSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ['id', 'first_name', 'last_name', 'email']
    
class PetOwnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ['first_name', 'last_name', 'address', 'email', 'phone']
    
# ?Pet Serializers
class PetListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['name', 'type']

class PetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'type','owner']


# ?Dates Serializers
class PetDateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ['datetime','type','pet']

class PetDatePetListModelSerializer(serializers.ModelSerializer):
    pet = PetModelSerializer()
    
    class Meta:
        model = PetDate
        fields = ['datetime','type','pet']

class PetDatePartialUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = ['datetime', 'type']


