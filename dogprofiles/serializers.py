from rest_framework import serializers
from profiles.models import Profile
from .models import DogProfile
# from dogprofiles.models import DogProfile


class DogProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    dog_profile_id = serializers.SerializerMethodField()
    profile_id = serializers.SerializerMethodField(source='owner.profile.id')

    dog_name = serializers.SerializerMethodField()
    dog_age = serializers.SerializerMethodField()
    dog_color = serializers.SerializerMethodField()
    dog_bio = serializers.SerializerMethodField()
    dog_image = serializers.ReadOnlyField(source='owner.profile.dog.image.url')

    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_dog_profile_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            dog = DogProfile.objects.filter(
                owner=user, dog_profile_id=obj.owner
            ).first()
            return dog_profile_id.id if following else None
        return None

    class Meta:
        model = DogProfile
        fields = [
            'dog_profile_id'
            'dog_name',
            'dog_age',
            'dog_color',
            'dog_bio',
            'dog_image',
            'id', 'profile_id', 'owner', 'created_at', 'updated_at', 'is_owner',
        ]


class DogProfileDetailSerializer(DogProfileSerializer):
    profile = serializers.ReadOnlyField(source='profile.id')
