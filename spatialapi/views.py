from rest_framework import viewsets
from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Exclude PATCH and DELETE methods
        if self.request.method in ['PATCH', 'DELETE']:
            queryset = queryset.none()
        return queryset
