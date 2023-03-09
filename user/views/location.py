from rest_framework.viewsets import ModelViewSet

from user.models import Location
from user.serializers import LocationSerializer


class LocViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
