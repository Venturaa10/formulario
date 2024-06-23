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
    form = ClienteForm(request.POST) #Instanciando o objeto ClienteForm em uma variavel 

    if form.is_valid():
        nome_form = form['nome'].value() # Recebendo o valor de 'nome' (esse é o widgets do forms.py) fornecido pelo cliente no formulario (index.html) e armazenando na variavel 'nome_form'
        sobrenome_form = form['sobrenome'].value()
        sexo_form = form['sexo'].value()
        idade_form = form['idade'].value()
        email_form = form['email'].value()
        telefone_form = form['telefone'].value()
        comentario_form = form['comentario'].value()
        ativo_form = form['ativo'].value()


        Cliente.objects.create(
            nome=nome_form, # Recebendo a variavel 'nome_form' e armazenando em 'nome' que é um dos atributos do model 'Cliente'
            sobrenome=sobrenome_form,
            sexo=sexo_form,
            idade=idade_form,
            email=email_form,
            telefone=telefone_form,
            comentario=comentario_form,
            ativo=ativo_form,
        ) # Todos os parametros são para criar o cliente e armazenar suas informações de acordo com os valores recebidas no formulario no qual o cliente preencheu.

        return redirect('index')
