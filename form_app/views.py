from django.shortcuts import render, redirect
from form_app.forms import ClienteForm
from django.contrib.auth.models import User
from form_app.models import Cliente
from django.contrib import messages # Importando o modulo responsavél por retornar mensagens ao usuario


def index(request):
    '''Exibe a pagina de cadastro e os inputs a serem preenchidos pelo Cliente'''
    form = ClienteForm()

    return render(request,'index.html', {'form': form})

def cadastro(request):
    form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        nome_form = form['nome'].value()

        if form.is_valid():
            form.save()
            messages.success(request, f'{nome_form} cadastrado(a) com sucesso!')
            return redirect('index')

        else:
            messages.error(request, f'Erro ao cadastrar {nome_form}, verifique as informações fornecidas!')
            print(form.errors) 

    else:
        '''Caso ocorra o envio de alguma informação invalida, não será feita a criação do Cliente, preciso adicionar uma mensagem indicando o erro aqui'''
        form = ClienteForm()

    return render(request,'index.html', {'form': form})
