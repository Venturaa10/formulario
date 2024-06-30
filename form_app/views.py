from django.shortcuts import render, redirect
from form_app.forms import ClienteForm
from django.contrib.auth.models import User
from form_app.models import Cliente
from django.contrib import auth # Importando o modulo para realizar a autenticação
from django.contrib import messages # Importando o modulo responsavél por retornar mensagens ao usuario


def index(request):
    '''Exibe a pagina de cadastro e os inputs a serem preenchidos pelo Cliente'''
    form = ClienteForm()

    return render(request,'index.html', {'form': form})

def cadastro(request):
    form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            '''O "cleaned_data" deve ser feita depois de verificar se o form é válido, ou seja, dentro de "form.is_valid()" '''
            nome_form = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']

            '''Verificando se o número de telefone e/ou email fornecido já exise no banco de dados, e retorna uma mensagem em caso de TRUE
            Evitando informações que devem ser exclusivas de cada cliente, sejam duplicadas
            A verificação é feita através de filtro (atributo_em_models=variavel_que_armazena_valor_do_form)
            '''
            if Cliente.objects.filter(email=email).exists():
                messages.error(request, 'O EMAIL fornecido já consta em nosso sistema!')
                return render(request,'index.html', {'form': form})

            elif Cliente.objects.filter(telefone=telefone).exists():
                messages.error(request, 'O NÚMERO DE TELEFONE fornecido já consta em nosso sistema')
                return render(request,'index.html', {'form': form})

            form.save()
            messages.success(request, f'{nome_form} cadastrado(a) com sucesso!')
            return redirect('index')

        else:
            messages.error(request, f'Erro ao cadastrar, verifique as informações fornecidas!')
            print(form.errors) 

    else:
        '''Caso ocorra o envio de alguma informação invalida, não será feita a criação do Cliente, preciso adicionar uma mensagem indicando o erro aqui'''
        form = ClienteForm()

    return render(request,'index.html', {'form': form})
