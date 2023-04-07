from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class DogProfile(models.Model):

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dog_name = models.CharField(max_length=255, blank=True)
    dog_age = IntegerField(default=0)
    dog_color = charField(max_length=255, blank=True)
    dog_bio = models.TextField(blank=True)
    dog_image = Imodels.ImageField(
        upload_to='images/', default='../default_dog-profile_gtehul.png'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s doggy profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
