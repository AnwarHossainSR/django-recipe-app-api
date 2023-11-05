from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('v1/auth/', include('user.urls')),
    path('admin/', admin.site.urls),
]
