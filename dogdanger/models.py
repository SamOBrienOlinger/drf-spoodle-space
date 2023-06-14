from django.db import models
from django.contrib.auth.models import User


class DogDanger(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bites_babies = models.TextField(blank=True)
    bites_kids = models.TextField(blank=True)
    bites_teenagers = models.TextField(blank=True)
    bites_burglars = models.TextField(blank=True)
    dangerously_cute = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s doggy danger level"


def create_dogdanger(sender, instance, created, **kwargs):
    if created:
        DogDanger.objects.create(owner=instance)
