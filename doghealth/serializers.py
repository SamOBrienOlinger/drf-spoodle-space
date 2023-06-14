from dogprofiles.models import DogProfile
from rest_framework import serializers
from .models import DogHealth


class DogHealthSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_dog_health_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            doghealth = DogHealth.objects.filter(
                owner=user, doghealth=obj.owner
            ).first()
            return doghealth.id if following else None
        return None

    class Meta:
        model = DogHealth
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'is_owner',
            'vet_name',
            'vet_phone',
            'vet_email',
            'kennel_cough',
            'rabies',
            'allergies',
            # 'dogprofile_id',
        ]


class DogHealthDetailSerializer(DogHealthSerializer):
    # dogprofile_id = serializers.ReadOnlyField(source='dogprofile.id')
    class Meta:
        model = DogHealth
        fields = '__all__'
