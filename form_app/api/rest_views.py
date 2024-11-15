from form_app.api.serializers import ClienteSerializer
from rest_framework import viewsets
from form_app.models import Cliente

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    