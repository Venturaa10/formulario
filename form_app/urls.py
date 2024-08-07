from django.urls import path
from form_app.views import login, cadastro, exibir, editar, excluir, logout

urlpatterns = [
    path('', cadastro, name='cadastro' ),
    path('login', login, name='login'),
    path('exibir', exibir, name='exibir'),
    path('editar/<int:cliente_id>', editar, name='editar'),
    path('excluir/<int:cliente_id>', excluir, name='excluir'),
    path('logout', logout, name='logout'),
]