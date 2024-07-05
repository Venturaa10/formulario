from django.urls import path
from form_app.views import index, cadastro, exibir, editar, excluir

urlpatterns = [
    path('', index, name='index' ),
    path('cadastro', cadastro, name='cadastro'),
    path('exibir', exibir, name='exibir'),
    path('editar/<int:cliente_id>', editar, name='editar'),
    path('excluir/<int:cliente_id>', excluir, name='excluir'),
]