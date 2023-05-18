from django.contrib import admin
from .models import DogProfile


# admin.site.register(DogProfile)

@admin.register(DogProfile)
class DogProfileModel(admin.ModelAdmin):
    list_filter = ('owner', 'dog_name', 'dog_age', 'dog_color', 'dog_bio', 'dog_profile_image')
    list_display = ('owner', 'dog_name', 'dog_age', 'dog_color', 'dog_bio', 'dog_profile_image')
