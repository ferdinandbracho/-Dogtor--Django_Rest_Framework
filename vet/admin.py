from django.contrib import admin
from .models import Pet, PetOwner, PetDate

admin.site.register(Pet)
admin.site.register(PetOwner)
admin.site.register(PetDate)

# Register your models here.
