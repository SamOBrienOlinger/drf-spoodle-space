from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class DoggyDanger(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bites_babies = models.TextField(blank=True)
    bites_kids = models.TextField(blank=True)
    bites_teenagers = models.TextField(blank=True)
    bites_burglars = models.TextField(blank=True)
    bites_bono = models.TextField(blank=True)
    dangerously_cute = models.TextField(blank=True)
