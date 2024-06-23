from django.shortcuts import render, redirect
from form_app.forms import ClienteForm
from django.contrib.auth.models import User
from form_app.models import Cliente

# Create your views here.

def index(request):
    '''Exibe a pagina de cadastro'''
    form = ClienteForm()

    return render(request,'index.html', {'form': form})

def cadastro(request):
    form = ClienteForm(request.POST) #Instanciando o objeto CadastroUser em uma variavel 

    if form.is_valid():
        nome_form = form['nome'].value()
        sobrenome_form = form['sobrenome'].value()
        idade_form = form['idade'].value()
        email_form = form['email'].value()
        telefone_form = form['telefone'].value()
        comentario_form = form['comentario'].value()
        ativo_form = form['ativo'].value()

        cliente = Cliente.objects.create(
            nome=nome_form,
            sobrenome=sobrenome_form,
            idade=idade_form,
            email=email_form,
            telefone=telefone_form,
            comentario=comentario_form,
            ativo=ativo_form,
        )
        cliente.save() #Cadastrando / Salvando o usuario no banco de dados
            
        return redirect('index')
