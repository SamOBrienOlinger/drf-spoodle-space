from rest_framework import serializers
from .models import DogDanger


class DogDangerSerializer(serializers.ModelSerializer):

    class meta:
        model = dogDanger
        fields = [
            'owner',
            'id',
            'created_at',
            'updated_at',

            'bites_babies',
            'bites_kids',
            'bites_teenagers',
            'bites_burglars',
            'bites_bolsonaro',
            'bites_trump',
            'bites_thatcher',
            'bites_reagan',
            'bites_bush',
            'bites_wbush',
            'dangerously_cute',
        ]
