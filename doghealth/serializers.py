from dogprofiles.models import DogProfile
from rest_framework import serializers
from .models import DogHealth


class DogHealthSerializer(serializers.ModelSerializer):
    vet_email = serializers.EmailField(required=False, allow_blank=True, max_length=255)
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = DogHealth
        fields = [
            'id',
            'owner',
            'owner_id',
            'created_at',
            'updated_at',
            'is_owner',
            'vet_name',
            'vet_phone',
            'vet_email',
            'kennel_cough',
            'rabies',
            'allergies',
            'profile_id',
            'profile_image',

        ]


class DogHealthDetailSerializer(DogHealthSerializer):
    dogprofile_id = serializers.ReadOnlyField(source='dogprofile.id')

    class Meta:
        model = DogHealth
        fields = '__all__'
