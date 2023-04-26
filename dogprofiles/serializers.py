from rest_framework import serializers
from dogprofiles.models import DogProfile
# from profiles.models import Profile
from django.contrib.humanize.templatetags.humanize import naturaltime


class DogProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.SerializerMethodField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    # my_dog_name = serializers.ReadOnlyField(source='my_dog.username')
    # dogprofiling_id = serializers.SerializerMethodField()
    dog_name = serializers.SerializerMethodField()
    dog_age = serializers.SerializerMethodField()
    dog_color = serializers.SerializerMethodField()
    dog_bio = serializers.SerializerMethodField()
    dog_profile_image = serializers.ReadOnlyField(source='owner.dogprofile.image.url')

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

    def get_profile_id(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # def get_profile_id(self, obj):
    #     user = self.context['request'].user
    #     if user.is_authenticated:
    #         profiling = Profile.objects.filter(
    #             owner=user, profiled=obj.owner
    #         ).first()
    #         return profiling_id if profiling else None
    #     return None

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def get_dog_name(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_dog_age(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_dog_color(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_dog_bio(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_dog_profile_image(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = DogProfile
        fields = [

            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',

            # 'profiling_id',

            'dog_name',
            'dog_age',
            'dog_color',
            'dog_bio',
            'dog_profile_image',

            # 'my_dog',
            # 'my_dog_name'
        ]


# class DogProfileDetailSerializer(DogProfileSerializer):
#     dogprofile = serializers.ReadOnlyField(source='dogprofile.id')
