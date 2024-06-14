from rest_framework import permissions,viewsets

from rest_framework.permissions import IsAuthenticated

from mechanic_management.api.serializers import MechanicEarningsSerializer, MechanicSerializer, MechanicWorkSerializer


class MechanicSerializerViewset(viewsets.ModelViewSet):
    serializer_class=MechanicSerializer
    queryset=MechanicSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]

class MechanicWorkSerializerViewset(viewsets.ModelViewSet):
    serializer_class=MechanicWorkSerializer
    queryset=MechanicWorkSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]

class MechanicEarningsSerializerViewset(viewsets.ModelViewSet):
    serializer_class=MechanicEarningsSerializer
    queryset=MechanicEarningsSerializer.Meta.model.objects.all()
    permission_classes=[IsAuthenticated]