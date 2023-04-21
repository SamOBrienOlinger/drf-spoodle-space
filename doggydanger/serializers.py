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
                'dangerously_cute'
            ]
