from django.shortcuts import render, redirect
from form_app.forms import CadastroUser
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    '''Exibe a pagina de cadastro'''
    form = CadastroUser()

    return render(request,'index.html', {'form': form})

def cadastro(request):
    form = CadastroUser(request.POST) #Instanciando o objeto CadastroUser em uma variavel 

    if form.is_valid():
        nome = form['nome_user'].value()
        sobrenome = form['sobrenome_user'].value()
        email = form['email_user'].value()
        comentario = form['comentario_user'].value()

        cadastro_usuario = User.objects.create_user(
            username=nome,
            email=email,
        )
        
        cadastro_usuario.save() #Cadastrando / Salvando o usuario no banco de dados
            
        return redirect('index')
    
def valida_nome(request):
    pass