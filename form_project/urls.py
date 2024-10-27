from django.contrib import admin
from django.urls import path, include
from form_app.views import ClienteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet, basename='Clientes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('form_app.urls')),
    path('root', include(router.urls)),
]
