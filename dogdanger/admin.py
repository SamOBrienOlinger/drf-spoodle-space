from django.contrib import admin
from .models import DogDanger


# admin.site.register(DogDanger)
@admin.register(DogDanger)
class DogDanger(admin.ModelAdmin):
    list_filter = ('owner', 'bites_babies', 'bites_kids', 'bites_teenagers', 'bites_burglars', 'dangerously_cute')
    list_display = ('owner', 'bites_babies', 'bites_kids', 'bites_teenagers', 'bites_burglars', 'dangerously_cute')
