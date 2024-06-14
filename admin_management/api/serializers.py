from rest_framework import serializers

from admin_management.models import AdminCommission
from customer_management.models import Customer
from mechanic_management.models import Mechanic


class AdminCommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminCommission
        fields="__all__"


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"


class MechanicsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mechanic
        fields="__all__"