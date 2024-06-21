from django.contrib import admin
from form_app.models import Cliente

# Register your models here.
class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'idade', 'email', 'ativo')
    
    list_display_links = ('id', 'nome')




admin.site.register(Cliente, Clientes)

