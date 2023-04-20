from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import IntegerField
from django.db.models import CharField


class DogProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    # owner = models.OneToOneField(User, related_name='doggy_profile', on_delete=models.CASCADE)
    # my_dog = models.OneToOneField(User, related_name='my_dog', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    dog_name = models.CharField(max_length=255, blank=True)
    dog_age = IntegerField(default=0)
    dog_color = CharField(max_length=255, blank=True)
    dog_bio = models.TextField(blank=True)
    # profile_image = models.ImageField(source='owner.profile.image.url')

    class Meta:
        ordering = ['-created_at']
        # unique_together = ['owner', 'my_dog']

    def __str__(self):
        return f"{self.owner}'s doggy profile"

    # def __str__(self):
        # return f"{self.owner} {self.my_dog}"


def create_dog_profile(sender, instance, created, **kwargs):
    if created:
        DogProfile.objects.create(owner=instance)


post_save.connect(create_dog_profile, sender=User)
