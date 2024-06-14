from rest_framework import serializers

from customer_management.models import Customer, Feedback, Notification, ServiceRequest, Vehicle


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle
        fields="__all__"

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceRequest
        fields="__all__"

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields="__all__"

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields="__all__"

