from rest_framework import serializers
from dogprofiles.models import DogProfile
from profiles.models import Profile
from django.contrib.humanize.templatetags.humanize import naturaltime
from followers.models import Follower


class DogProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    profile_id = serializers.SerializerMethodField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    dogprofile_id = serializers.SerializerMethodField(
        source='owner.dogprofile.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner).first()
            return following.id if following else None
        return None

    def get_dogprofile_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            dogprofile = DogProfile.objects.filter(owner=user).first()
            return dogprofile.id if dogprofile else None
        return None

    def get_profile_id(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = DogProfile
        fields = '__all__'
