from django.contrib import admin
from .models import DogHealth


@admin.register(DogHealth)
class DogHealthModel(admin.ModelAdmin):
    list_filter = ('owner', 'vet_name', 'vet_phone', 'vet_email', 'kennel_cough', 'rabies', 'allergies')
    list_display = ('owner', 'vet_name', 'vet_phone', 'vet_email', 'kennel_cough', 'rabies', 'allergies')
