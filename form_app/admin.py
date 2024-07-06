from django.contrib import admin
from form_app.models import Cliente

# Register your models here.
class Clientes(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','idade', 'email','cpf','sexo','telefone','ativo')    
    list_display_links = ('id', 'nome')
    list_per_page = 10

admin.site.register(Cliente, Clientes)

