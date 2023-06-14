from dogprofiles.models import DogProfile
from rest_framework import serializers
from .models import DogDanger


class DogDangerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_dog_danger_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            dogdanger = DogDanger.objects.filter(
                owner=user, dogdanger=obj.owner
            ).first()
            return dogdanger.id if following else None
        return None

    class Meta:
        model = DogDanger
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'is_owner',
            'bites_babies',
            'bites_kids',
            'bites_teenagers',
            'bites_burglars',
            'dangerously_cute',
        ]


class DogDangerDetailSerializer(serializers.ModelSerializer):
    # dogprofile = serializers.ReadOnlyField(source='dogprofile.id')
    class Meta:
        model = DogDanger
        fields = '__all__'
