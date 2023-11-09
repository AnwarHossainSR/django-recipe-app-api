from rest_framework.routers import SimpleRouter
from .views import DownloadKMLDrawings, DownloadKMZDrawings, LocationViewSet
from django.urls import path

router = SimpleRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = [
    *router.urls,  # Include generated viewset routes
    path('download/drawings/kml', DownloadKMLDrawings.as_view(), name='download_kml_drawings'),
    path('download/drawings/kmz', DownloadKMZDrawings.as_view(), name='download_kmz_drawings'),
]