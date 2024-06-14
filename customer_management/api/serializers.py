from rest_framework import serializers

from customer_management.models import Customer, Feedback, Notification, ServiceRequest, Vehicle



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

class CustomerSerializer(serializers.ModelSerializer):
    vehicles = VehicleSerializer(many=True, read_only=True)
    service_requests = ServiceRequestSerializer(many=True, read_only=True)
    

    class Meta:
        model = Customer
        fields = "__all__"
        
    