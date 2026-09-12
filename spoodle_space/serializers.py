from allauth.account.adapter import get_adapter
from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    @staticmethod
    def validate_username(username):
        # UniqueValidator excludes the current account. The adapter's default
        # lookup does not, so only run its non-uniqueness checks here.
        return get_adapter().clean_username(username, shallow=True)

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
        extra_kwargs = {
            'username': {
                # Replace the model's character whitelist while retaining the
                # field's required/blank/length checks and account uniqueness.
                'validators': [
                    UniqueValidator(
                        queryset=get_user_model().objects.all(),
                        lookup='iexact',
                        message='A user with that username already exists.',
                    ),
                ],
                'help_text': (
                    'Spaces, numbers, special characters and emojis are welcome. '
                    'Use a unique name, up to 150 characters.'
                ),
            },
        }
