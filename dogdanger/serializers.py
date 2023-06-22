from dogprofiles.models import DogProfile
from rest_framework import serializers
from .models import DogDanger


class DogDangerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.SerializerMethodField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_profile_id(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = DogDanger
        fields = [
            'id',
            'owner',
            'owner_id',
            'created_at',
            'updated_at',
            'is_owner',
            'bites_babies',
            'bites_kids',
            'bites_teenagers',
            'bites_burglars',
            'dangerously_cute',
            'profile_id',
            'profile_image',
        ]


class DogDangerDetailSerializer(DogDangerSerializer):
    dogprofile = serializers.ReadOnlyField(source='dogprofile.id')

    class Meta:
        model = DogDanger
        fields = '__all__'
