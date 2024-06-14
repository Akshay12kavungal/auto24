from rest_framework import serializers

from admin_management.models import AdminCommission


class AdminCommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminCommission
        fields="__all__"
