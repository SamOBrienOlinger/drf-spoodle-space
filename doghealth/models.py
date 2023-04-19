from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class DogHealth(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    vet_name = models.CharField(max_length=255, blank=True)
    vet_phone = models.CharField(max_length=255, blank=True)
    vet_email = models.CharField(max_length=255, blank=True)
    chipped = models.CharField(max_length=255, blank=True)
    kennel_cough = models.CharField(max_length=255, blank=True)
    rabies = models.CharField(max_length=255, blank=True)
    allergies = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'vet_name']

    def __str__(self):
        return f"{self.owner}'s Dog's health status"


def create_doghealth(sender, instance, created, **kwargs):
    if created:
        DogHealth.objects.create(owner=instance)


post_save.connect(create_doghealth, sender=User)
