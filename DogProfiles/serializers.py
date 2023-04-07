from rest_framework import serializers
# from .models import Profile
from .models import DogProfile
# from followers.models import Follower


class DogProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    dog_name = serializers.SerializerMethodField(source='owner.dog.name')
    dog_age = serializers.SerializerMethodField()
    dog_color = serializers.SerializerMethodField()
    dog_bio = serializers.SerializerMethodField()
    dog_image = serializers.ReadOnlyField(source='owner.dog.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # def get_following_id(self, obj):
    #     user = self.context['request'].user
    #     if user.is_authenticated:
    #         following = Follower.objects.filter(
    #             owner=user, followed=obj.owner
    #         ).first()
    #        print(following)
        #     return following.id if following else None
        # return None

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

        class Meta:
            model = DogProfile
            fields = [
                'dog_name',
                'dog_age',
                'dog_color',
                'dog_bio',
                'dog_image',
                'id', 'owner', 'created_at', 'updated_at', 'is_owner',
            ]
