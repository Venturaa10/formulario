from django.shortcuts import render, redirect
from form_app.forms import ClienteForm, LoginForm
from django.contrib.auth.models import User
from form_app.models import Cliente
from django.contrib import auth, messages # Importa o modulo para realizar a autenticação
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator # Paginação
import re



def login(request): 
    '''Função reponsavel por pedir o login ao usuario para liberar o acesso as informações dos clientes cadastrados'''
    form = LoginForm()
    if request.method == 'POST': # Condição so será executada se for requisitado, ou seja, botão interagido 
        form = LoginForm(request.POST) # Recria o formulario com os dados enviados pelo usuario, por isso é utilizado o "request.POST" como parametro

        if form.is_valid():
            # Recupera os valores fornecidos no formulario
            nome = form['nome_login'].value() 
            senha = form['senha'].value()

            # Faz a autenticação para saber se o usuario existe
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )

            if usuario is not None:
                # Se o usuário for autenticado com sucesso (usuario não é "None"), realiza o login e redireciona para o template exibir
                auth.login(request, usuario)
                messages.add_message(request, messages.INFO,f'{nome} logado com sucesso!', extra_tags='info_login') 
                return redirect('exibir')
            else:
                # Se a autenticação falhar, exibe uma mensagem de erro e redireciona de volta para a página de login
                messages.add_message(request, messages.ERROR, 'Erro ao efetuar login!', extra_tags='error_login')
                return redirect('login')
        else:
           pass

    return render(request, 'form_app/login.html', {'form': form})


def cadastro(request):
    form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            # O "cleaned_data" deve ser feita depois de verificar se o form é válido, ou seja, dentro de "form.is_valid()" 
            nome_form = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            celular = form.cleaned_data['celular']

            # Verifica se o número de celular e/ou email fornecido já exise no banco de dados, e retorna uma mensagem em caso de TRUE, evitando informações que devem ser exclusivas de cada cliente, sejam duplicadas
            # A verificação é feita através de filtro (atributo_em_models=variavel_que_armazena_valor_do_form)

            if Cliente.objects.filter(email=email).exists():
                # Retorna mensagem de erro em caso de email já cadastrado anteriormente
                messages.add_message(request, messages.INFO,'O EMAIL fornecido já consta em nosso sistema!', extra_tags='cadastro')
                return render(request,'cadastro.html', {'form': form})

            elif Cliente.objects.filter(celular=celular).exists():
                messages.add_message(request, messages.INFO,'O NÚMERO DE CELULAR fornecido já consta em nosso sistema', extra_tags='cadastro')
                return render(request,'cadastro.html', {'form': form})

            form.save()
            messages.add_message(request, messages.SUCCESS,f'Cadastro de {nome_form} realizado com sucesso!', extra_tags='cadastro')
            return redirect('cadastro')

        else:
            messages.add_message(request, messages.ERROR,f'Erro ao cadastrar, verifique as informações fornecidas!', extra_tags='cadastro')

    else:
        form = ClienteForm()

    return render(request,'form_app/cadastro.html', {'form': form})


@login_required(login_url='login') # Linha responsavel por impedir que usuario acesse o sistema sem estar logado
def exibir(request):
    '''
    --> Exibe e o número de clientes cadastrados no sistema
    --> Função responsavel por realizar a exibição dos clientes, paginação e a busca do cliente pelo CPF
    --> limpa_cpf_busca -> Recebe e armazena o cpf a ser consultado. 1º Parametro é o "cpf", associado ao nome dado ao atributo "name" na tag "input".
    --> buscar_cpf -> Limpa o cpf informado, removendo pontuações, simbolos e espaços em branco.
    --> clietes -> Recupera todos os clientes e ordena com base no nome 
    --> total_clientes -> Total de clientes armazenados no banco de dados
    '''
    limpa_cpf_busca = request.POST.get('cpf', '').strip()
    buscar_cpf = re.sub(r'[^a-zA-Z0-9]', '', limpa_cpf_busca) 
    clientes = Cliente.objects.all().order_by('nome') 
    total_clientes = clientes.count() 

    if request.method == 'POST': 
        if buscar_cpf: 
            clientes = Cliente.objects.filter(cpf__icontains=buscar_cpf).order_by('nome') # Filtra clientes pelo CPF
            if clientes.exists():
                messages.add_message(request, messages.SUCCESS, 'Cliente localizado no sistema!', extra_tags='buscar')
            
            else:
                clientes = Cliente.objects.all().order_by('nome') # Retorna todos os clientes em caso de não localizado
                messages.add_message(request, messages.ERROR, 'Cliente não localizado no sistema!', extra_tags='buscar')

        else:
            clientes = Cliente.objects.all().order_by('nome') # Retorna todos os clientes em caso de cpf não mencionado, mas botão para buscar interagido
            messages.add_message(request, messages.INFO, 'Informe o CPF do cliente!', extra_tags='buscar')

    # Paginação dos clientes
    paginator = Paginator(clientes, 8) # Cliente por pagina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'form_app/exibir.html', {'page_obj': page_obj, 'query': buscar_cpf, 'total_clientes': total_clientes})


@login_required(login_url='login')
def editar(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)# Armazena a id do cliente
    dados = ClienteForm(instance=cliente)
    if request.method == 'POST':
        dados = ClienteForm(request.POST, instance=cliente)

        if dados.is_valid():
            nome_form = dados.cleaned_data['nome']

            dados.save()
            messages.add_message(request, messages.INFO, f'Dados de "{nome_form}" atualizados!', extra_tags='editar')
            return redirect('exibir')

    return render(request, 'form_app/editar.html', {'dados':dados, 'cliente_id': cliente_id})


@login_required(login_url='login')
def excluir(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    nome_cliente = cliente.nome # Armazena nome do cliente que foi excluído
    cpf_cliente = cliente.cpf
    cliente.delete() # Deleta o objeto do banco de dados
    
    messages.add_message(request, messages.ERROR,f'Cliente "{nome_cliente}", cujo cpf é "{cpf_cliente}", foi excluído do sistema!', extra_tags='excluir')
    return redirect('exibir')


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS,'Logout efetuado com sucesso', extra_tags='logout') 
    return redirect('login')
