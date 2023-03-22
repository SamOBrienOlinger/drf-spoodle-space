from rest_framework import serializers
from likes.models import Like
from django.db import IntegrityError


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Like()
        fields = [
            'id', 'owner', 'created_at', 'post'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible cocka-duplicate'})
