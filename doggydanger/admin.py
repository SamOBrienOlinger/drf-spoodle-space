from django.contrib import admin
from .models import DoggyDanger


# admin.site.register(DoggyDanger)
@admin.register(DoggyDanger)
class DoggyDanger(admin.ModelAdmin):
    list_filter = ('owner', 'bites_babies', 'bites_kids', 'bites_teenagers', 'bites_burglars', 'bites_bolsonaro', 'bites_trump', 'bites_thatcher', 'bites_reagan', 'bites_bush', 'bites_wbush', 'dangerously_cute')
    list_display = ('owner', 'bites_babies', 'bites_kids', 'bites_teenagers', 'bites_burglars', 'bites_bolsonaro', 'bites_trump', 'bites_thatcher', 'bites_reagan', 'bites_bush', 'bites_wbush', 'dangerously_cute')
