from form_app.api.serializers import ClienteSerializer
from rest_framework import viewsets, filters
from form_app.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend # run: pip install django-filter

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # Filtros da API
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome'] 
    search_fields = ['nome', 'cpf'] # Dados que podem ser buscados no campo de busca
