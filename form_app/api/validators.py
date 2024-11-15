'''Arquivo responsavel pelas validações dos campos do serializers '''
import re
from validate_docbr import CPF

def nome_invalido(nome):
    # Funciona
    return not nome.isalpha()

def sobrenome_invalido(sobrenome):
    # Funciona
    return not sobrenome.isalpha()

def email_invalido(email):
    # Funciona
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    resposta_email = re.findall(email_regex, email)
    return not resposta_email

def cpf_invalido(numero_cpf):
    # Funcionando
    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido

def celular_invalido(celular):
    # Funciona
    # Se padrão for true, retorna o valor encontrado, se não, retorna uma lista vazia.
    regex_celular = r'^[0-9]{2,3}[0-9]{5}[0-9]{4}$'
    resposta_celular = re.findall(regex_celular,celular) # Busca modelo na variavel celular.   
    return not resposta_celular
        
