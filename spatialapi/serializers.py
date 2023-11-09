from rest_framework_gis.serializers import GeoFeatureModelSerializer

from rest_framework import serializers
from .models import Location


class LocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Location
        geo_field = 'geom'
        fields = ('id', 'name', 'description', 'address',
                  'geom', 'created_at', 'updated_at')

class DownloadKMZDrawingsSerializer(serializers.Serializer):
    pass