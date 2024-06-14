from rest_framework import permissions,viewsets

from admin_management.api.serializers import AdminCommissionSerializer, CustomersSerializer, MechanicsSerializer
from rest_framework.permissions import IsAuthenticated



class AdminCommissionSerializerViewset(viewsets.ModelViewSet):
    serializer_class=AdminCommissionSerializer
    queryset=AdminCommissionSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]
    

class CustomersSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomersSerializer
    queryset = CustomersSerializer.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]


class MechanicsSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = MechanicsSerializer
    queryset = MechanicsSerializer.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]





