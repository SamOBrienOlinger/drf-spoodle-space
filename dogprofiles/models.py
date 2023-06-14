from django.db import models
from django.contrib.auth.models import User


class DogProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dog_name = models.TextField(max_length=255, blank=True)
    dog_age = models.TextField(blank=True)
    dog_color = models.TextField(blank=True)
    dog_bio = models.TextField(blank=True)
    dog_profile_image = models.ImageField(upload_to='images/', default='../default_dog-profile_gtehul.png', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s doggy profile"


def create_dogdanger(sender, instance, created, **kwargs):
    if created:
        DogDanger.objects.create(owner=instance)
