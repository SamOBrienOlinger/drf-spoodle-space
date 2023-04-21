from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class DoggyDanger(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# bites_babies
# bites_kids
# bites_teenagers
# bites_burglars
# bites_bono
# Dangerously_cute
# Fluffy_threat
