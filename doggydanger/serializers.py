from rest_framework import serializers
from .models import DoggyDanger


class DoggyDangerSerializer(serializers.ModelSerializer):

    class meta:
        model = DoggyDanger
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
