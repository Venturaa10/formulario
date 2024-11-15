from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('form_app.urls')),
    path('api/', include('form_app.api.urls')),
]
