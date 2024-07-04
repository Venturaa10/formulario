from django.urls import path
from form_app.views import index, cadastro, exibir

urlpatterns = [
    path('', index, name='index' ),
    path('cadastro', cadastro, name='cadastro'),
    path('exibir', exibir, name='exibir'),
]