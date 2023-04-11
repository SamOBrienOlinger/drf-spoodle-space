from rest_framework import serializers
# from .models import Profile
from .models import DogProfile
# from DogProfiles.models import DogProfile


class DogProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    # dog_profile_id = serializers.SerializerMethodField(source='owner.dog.profile.id')
    profile_id = serializers.SerializerMethodField(source='owner.profile.id')

    dog_name = serializers.SerializerMethodField()
    dog_age = serializers.SerializerMethodField()
    dog_color = serializers.SerializerMethodField()
    dog_bio = serializers.SerializerMethodField()
    dog_image = serializers.ReadOnlyField(source='owner.profile.dog.image.url')

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_dog_name(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            dog_name = DogProfile.objects.filter(
                owner=user, DogProfile=obj.owner
            ).first()
            # print(dog_name)
            return dog_profile_id if following else None
        return None

    class Meta:
        model = DogProfile
        fields = [
            'dog_name',
            'dog_age',
            'dog_color',
            'dog_bio',
            'dog_image',
            'id', 'profile_id', 'owner', 'created_at', 'updated_at', 'is_owner',
        ]


class DogProfileDetailSerializer(DogProfileSerializer):
    profile = serializers.ReadOnlyField(source='profile.id')
