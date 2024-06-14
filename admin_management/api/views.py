from rest_framework import permissions,viewsets

from admin_management.api.serializers import AdminCommissionSerializer
from rest_framework.permissions import IsAuthenticated


class AdminCommissionSerializerViewset(viewsets.ModelViewSet):
    serializer_class=AdminCommissionSerializer
    queryset=AdminCommissionSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]
    





