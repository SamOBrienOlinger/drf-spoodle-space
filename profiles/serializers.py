from rest_framework import serializers
from .models import Profile
from dogprofiles.models import DogProfile
from doghealth.models import DogHealth
from dogdanger.models import DogDanger
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    dog_profile = serializers.SerializerMethodField()
    dog_health = serializers.SerializerMethodField()
    dog_danger = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            # print(following)
            return following.id if following else None
        return None

    def get_dog_profile(self, obj):
        try:
            return DogProfile.objects.get(owner=obj.pk).pk
        except Exception as e:
            return None

    def get_dog_health(self, obj):
        try:
            return DogHealth.objects.get(owner=obj.pk).pk
        except Exception as e:
            return None

    def get_dog_danger(self, obj):
        try:
            return DogDanger.objects.get(owner=obj.pk).pk
        except Exception as e:
            return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'following_id',
            'posts_count', 'followers_count', 'following_count', 'dog_profile',
            'dog_health', 'dog_danger'
        ]
