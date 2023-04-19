from dogprofiles.models import DogProfile
from rest_framework import serializers
from .models import DogHealth


class DogHealthSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    dog_profile_id = serializers.SerializerMethodField()
    # profile_id = serializers.SerializerMethodField(source='owner.profile.id')


def get_is_owner(self, obj):
    request = self.context['request']
    return request.user == obj.owner


def get_dog_health_id(self, obj):
    user = self.context['request'].user
    if user.is_authenticated:
        doghealth = DogHealth.objects.filter(
            owner=user, doghealth=obj.owner
        ).first()
        return dog_health_id.id if following else None
    return None


class Meta:
    model = DogHealth
    fields = [
        'vet_name'
        'vet_phone'
        'vet_email'
        'chipped'
        'kennel_cough'
        'rabies'
        'allergies'
        'id', 'owner', 'created_at', 'updated_at', 'is_owner',
    ]
# 'dogprofile_id',
# 'dog_health_id'


class DogHealthDetailSerializer(DogHealthSerializer):
    profile = serializers.ReadOnlyField(source='dogprofile.id')

    # dogprofile = serializers.ReadOnlyField(source='dogprofile.id')
