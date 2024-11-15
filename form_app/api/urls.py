from django.urls import path, include
from form_app.api.rest_views import ClienteViewSet
from rest_framework.routers import DefaultRouter

'''
Rotas para API:
http://127.0.0.1:8000/api/ -> Visualizar todas as rotas disponiveis na API.
http://127.0.0.1:8000/api/clientes/ -> Endpoint das APIs de clientes, lista todos os clientes ou cria um novo cliente.
http://127.0.0.1:8000/api/clientes/id/ -> Endpoint de um cliente especifico atraves do id.
'''

router = DefaultRouter()
router.register('clientes', ClienteViewSet, basename='clientes')

urlpatterns = [
    path('', include(router.urls)), # Inclui todas as rotas geradas pelo router
]