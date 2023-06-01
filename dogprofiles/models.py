from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class DogProfile(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
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


# def create_dog_profile(sender, instance, created, **kwargs):
#     if created:
#         DogProfile.objects.create(owner=instance)

# def create_dog_profile(sender, instance, created, **kwargs):
#     if created and not DogProfile.objects.filter(owner=instance).exists():
#         DogProfile.objects.create(owner=instance)


# post_save.connect(create_dog_profile, sender=User)

def create_dog_profile(sender, instance, created, **kwargs):
    if created:
        dog_profile, _ = DogProfile.objects.get_or_create(owner=instance)
        dog_profile.dog_name = ""
        dog_profile.dog_age = ""
        dog_profile.dog_color = ""
        dog_profile.dog_bio = ""
        dog_profile.save()


post_save.connect(create_dog_profile, sender=User)
