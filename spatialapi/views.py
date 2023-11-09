from rest_framework import viewsets

from utils.render import CustomRenderer
from .models import Location
from .serializers import DownloadKMZDrawingsSerializer, LocationSerializer
from django.http import HttpResponse
import simplekml
import zipfile
from rest_framework.views import APIView
import tempfile
import os

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Exclude PATCH and DELETE methods
        if self.request.method in ['PATCH', 'DELETE']:
            queryset = queryset.none()
        return queryset
    
class DownloadKMLDrawings(APIView):
    serializer_class = DownloadKMZDrawingsSerializer(many=True)
    
    def get(self, request, *args, **kwargs):
        kml = simplekml.Kml()

        # Get the drawings data from the database or any other source
        drawings_data = Location.objects.values('name', 'geom')

        for drawing_data in drawings_data:
            # Assuming drawing_data contains 'name' and 'geom' fields
            kml.newpoint(name=drawing_data['name'], coords=[(drawing_data['geom'].x, drawing_data['geom'].y)])

        # Create a temporary file to save the KML content
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".kml")
        temp_file_path = temp_file.name

        # Save the KML content to the temporary file
        kml.save(temp_file_path)
        temp_file.close()

        # Read the content of the temporary file
        with open(temp_file_path, 'rb') as kml_file:
            kml_content = kml_file.read()

        # Delete the temporary file after reading its content
        os.unlink(temp_file_path)

        # Create HttpResponse with KML content
        response = HttpResponse(kml_content, content_type='application/kml')
        response['Content-Disposition'] = 'attachment; filename="drawings.kml"'
        return response






class DownloadKMZDrawings(APIView):
    serializer_class = DownloadKMZDrawingsSerializer(many=True)
    def get(self, request, *args, **kwargs):
        kml = simplekml.Kml()

        # Get the drawings data from the database or any other source
        drawings_data = Location.objects.values('name', 'geom')

        for drawing_data in drawings_data:
            # Assuming drawing_data contains 'name' and 'geom' fields
            kml.newpoint(name=drawing_data['name'], coords=[(drawing_data['geom'].x, drawing_data['geom'].y)])

        kml_content = kml.kml()

        # Create KMZ file by adding KML content to a zip archive
        response = HttpResponse(content_type='application/kmz')
        response['Content-Disposition'] = 'attachment; filename="drawings.kmz'

        with zipfile.ZipFile(response, 'w') as kmz_file:
            kmz_file.writestr('drawings.kml', kml_content)

        return response
