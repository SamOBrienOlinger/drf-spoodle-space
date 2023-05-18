from rest_framework import serializers
from dogprofiles.models import DogProfile
from profiles.models import Profile
from django.contrib.humanize.templatetags.humanize import naturaltime
from followers.models import Follower


class DogProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    following_id = serializers.SerializerMethodField()

    profile_id = serializers.SerializerMethodField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    # created_at = serializers.SerializerMethodField()
    # updated_at = serializers.SerializerMethodField()
    # dog_name = serializers.SerializerMethodField()
    # dog_age = serializers.SerializerMethodField()
    # dog_color = serializers.SerializerMethodField()
    # dog_bio = serializers.SerializerMethodField()
    dogprofile_id = serializers.SerializerMethodField(source='owner.dogprofile.id')
    # image = serializers.ReadOnlyField(source='owner.dogprofile.image.url')

    image = serializers.ReadOnlyField(source='owner.dogprofile.image.url')

    # dogs_name = serializers.ReadOnlyField()
    # dogs_age = serializers.ReadOnlyField()
    # dogs_color = serializers.ReadOnlyField()
    # dogs_bio = serializers.ReadOnlyField()

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

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    def get_dogprofile_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            dogprofile = DogProfile.objects.filter(
                owner=user
            ).first()
            return dogprofile.id if dogprofile else None
        return None

    def get_profile_id(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    # def get_dog_name(self, obj):
    #     user = self.context['request'].user
    #     if user.is_authenticated:
    #         like = Like.objects.filter(
    #             owner=user, post=obj
    #         ).first()
    #         return like.id if like else None
    #     return None

    # def get_dogs_name(self, obj):
    #     request = self.context['request']
    #     return request.user == obj.owner

    # def get_dogs_age(self, obj):
    #     request = self.context['request']
    #     return request.user == obj.owner

    # def get_dogs_color(self, obj):
    #     request = self.context['request']
    #     return request.user == obj.owner

    # def get_dogs_bio(self, obj):
    #     request = self.context['request']
    #     return request.user == obj.owner

    # def get_dogs_profile_image(self, obj):
    #     request = self.context['request']
    #     return request.user == obj.owner

    class Meta:
        model = DogProfile
        fields = [

            'id',
            'owner',
            'is_owner',

            'following_id',

            'created_at',
            'updated_at',

            'profile_id',
            'profile_image',

            'dogprofile_id',

            'dog_name',
            'dog_age',
            'dog_color',
            'dog_bio',
            'image',
        ]


# class DogProfileDetailSerializer(DogProfileSerializer):
#     dogprofile = serializers.ReadOnlyField(source='dogprofile.id')
