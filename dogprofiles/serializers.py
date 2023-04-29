from rest_framework import serializers
from dogprofiles.models import DogProfile
from django.contrib.humanize.templatetags.humanize import naturaltime


class DogProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.SerializerMethodField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    # created_at = serializers.SerializerMethodField()
    # updated_at = serializers.SerializerMethodField()
    # dog_name = serializers.SerializerMethodField()
    # dog_age = serializers.SerializerMethodField()
    # dog_color = serializers.SerializerMethodField()
    # dog_bio = serializers.SerializerMethodField()
    dog_profile_image = serializers.ReadOnlyField(source='owner.dogprofile.image.url')

    # dogs_name = serializers.SerializerMethodField()
    # dogs_age = serializers.SerializerMethodField()
    # dogs_color = serializers.SerializerMethodField()
    # dogs_bio = serializers.SerializerMethodField()

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

    # def get_created_at(self, obj):
    #     return naturaltime(obj.created_at)

    # def get_updated_at(self, obj):
    #     return naturaltime(obj.updated_at)

    def get_dogs_name(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_dogs_age(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_dogs_color(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_dogs_bio(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_dogs_profile_image(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = DogProfile
        fields = [

            'id',
            'owner',
            'is_owner',
            'created_at',
            'updated_at',
            
            'profile_id',
            'profile_image',

            'dog_name',
            'dog_age',
            'dog_color',
            'dog_bio',
            'dog_profile_image',
        ]


# class DogProfileDetailSerializer(DogProfileSerializer):
#     dogprofile = serializers.ReadOnlyField(source='dogprofile.id')
