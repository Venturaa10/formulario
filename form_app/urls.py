from django.urls import path
from form_app.views import index, cadastro

urlpatterns = [
    path('', index, name='index' ),
    path('cadastro', cadastro, name='cadastro'),
]