from django.shortcuts import render, redirect
from form_app.forms import ClienteForm
from django.contrib.auth.models import User
from form_app.models import Cliente
from django.contrib import messages # Importando o modulo responsavél por retornar mensagens ao usuario

# Create your views here.

def index(request):
    '''Exibe a pagina de cadastro e os inputs a serem preenchidos pelo Cliente'''
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
        estado_form = form['estado'].value()
        telefone_form = form['telefone'].value()
        comentario_form = form['comentario'].value()
        ativo_form = form['ativo'].value()

        
        Cliente.objects.create(
            nome=nome_form, # Recebendo a variavel 'nome_form' e armazenando em 'nome' que é um dos atributos do model 'Cliente'
            sobrenome=sobrenome_form,
            sexo=sexo_form,
            idade=idade_form,
            email=email_form,
            estado=estado_form,
            telefone=telefone_form,
            comentario=comentario_form,
            ativo=ativo_form,
        ) # Todos os parametros são para criar o cliente e armazenar suas informações de acordo com os valores recebidas no formulario no qual o cliente preencheu.

        messages.success(request, f'{nome_form} cadastrado(a) com sucesso!')
        return redirect('index')

    else:
        '''Caso ocorra o envio de alguma informação invalida, não será feita a criação do Cliente, preciso adicionar uma mensagem indicando o erro aqui'''
        form = ClienteForm()

    return render(request,'index.html', {'form': form})
