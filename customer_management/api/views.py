from rest_framework import permissions,viewsets

from rest_framework.permissions import IsAuthenticated

from customer_management.api.serializers import CustomerSerializer, FeedbackSerializer, NotificationSerializer, ServiceRequestSerializer, VehicleSerializer
from customer_management.models import Customer



class CustomerSerializerViewset(viewsets.ModelViewSet):
    serializer_class=CustomerSerializer
    queryset=CustomerSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]
    

class VehicleSerializerViewset(viewsets.ModelViewSet):
    serializer_class=VehicleSerializer
    queryset=VehicleSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]

class ServiceRequestSerializerViewset(viewsets.ModelViewSet):
    serializer_class=ServiceRequestSerializer
    queryset=ServiceRequestSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]

class FeedbackSerializerViewset(viewsets.ModelViewSet):
    serializer_class=FeedbackSerializer
    queryset=FeedbackSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]

class NotificationSerializerViewset(viewsets.ModelViewSet):
    serializer_class=NotificationSerializer
    queryset=NotificationSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]


class CustomerProfileViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.customer