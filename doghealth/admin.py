from django.contrib import admin
from .models import DogHealth


# admin.site.register(DogHealth)
@admin.register(DogHealth)
class DogHealthModel(admin.ModelAdmin):
    list_filter = ('vet_phone', 'vet_email', 'chipped', 'kennel_cough', 'rabies', 'allergies')
    list_display = ('vet_phone', 'vet_email', 'chipped', 'kennel_cough', 'rabies', 'allergies')
