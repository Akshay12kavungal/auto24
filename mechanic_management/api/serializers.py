from rest_framework import serializers

from mechanic_management.models import Mechanic, MechanicEarnings, MechanicWork


class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mechanic
        fields="__all__"

class MechanicWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model=MechanicWork
        fields="__all__"


class MechanicEarningsSerializer(serializers.ModelSerializer):
    class Meta:
        model=MechanicEarnings
        fields="__all__"




        