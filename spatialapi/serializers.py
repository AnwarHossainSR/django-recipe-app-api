from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Location


class LocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Location
        geo_field = 'geom'
        fields = ('id', 'name', 'description', 'address',
                  'geom', 'created_at', 'updated_at')


# from rest_framework import serializers
# from .models import Location

# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = ('id', 'name', 'description', 'address', 'geom', 'created_at', 'updated_at')
