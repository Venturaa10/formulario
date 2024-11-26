# Nesse arquivo é destinado a fazer modificações em admin

from django.db import models
from datetime import datetime # Import para configurar e trabalhar com data e hora
from django.core.exceptions import ValidationError # Import para fazer validações
# django.core.validator é recomendado para trabalhar com validações,como expressoes regulares
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator, EmailValidator # Import para validar valores 
from validate_docbr import CPF, CNPJ


class Cliente(models.Model):
    OPCAO_SEXO = [
        ('I', 'Não Informado'),
        ('M', 'Masculino'), 
        ('F', 'Feminino'),
    ]

    OPCAO_ESTADOS_BRASIL = [
        ('E', 'Escolha...'),
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]
        # EXPLICAÇÃO DOS ATRIBUTOS
        # O comentario não é um campo obrigatorio, por isso dever ter "null" e "blank" como TRUE, pois por padrão o Django torna o preenchimento obrigatorio
        # unique=True -> O django garante que não ocorra informações dessas atributos com valores duplicados no banco de dados
    nome = models.CharField(max_length=45, null=False, blank=False, help_text='Nome do Cliente')
    sobrenome = models.CharField(max_length=45, null=False, blank=False, help_text='Sobrenome do Cliente')
    sexo = models.CharField(max_length=1, choices=OPCAO_SEXO, default='I')
    idade = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)],null=False, blank=False)
    email = models.EmailField(max_length=50,unique=True,null=False, blank=False, help_text='emailCliente@dominio.com', validators=[EmailValidator(message='Email fornecido é inválido!')])
    cpf = models.CharField(max_length=11,unique=True,null=False, blank=False, default='', help_text='11122233399', validators=[RegexValidator(r'^[0-9]{11}$', 'O "CPF" deve conter exatamente 11 números!')])
    estado = models.CharField(max_length=2, choices=OPCAO_ESTADOS_BRASIL, null=False, blank=False, default='E')
    celular = models.CharField(max_length=12,unique=True,null=False, blank=False, help_text='11900000000', validators=[RegexValidator(r'^[0-9]{2,3}[0-9]{5}[0-9]{4}$', 'O campo celular precisa seguir um modelo parecido com: 11900000000 (DDD + número sem espaços ou caracteres especiais).')])
    comentario = models.TextField(max_length=250, null=True, blank=True, help_text='Uma sugestão aqui :)')
    data_criacao = models.DateTimeField(default=datetime.now) # Atributo que exibe a data e a hora de criação do cliente
    status = models.BooleanField(default=True) # Atributo responsavel por indicar se o cliente está ativo ou não, o "default" indica que todo cliente cadastrado está com o status de "ativo".


    def clean(self):
        '''
        Metodo responsavél pela realização das validações dos atributos do model Cliente, recomendado para validações simples.
        raise é usado para lidar com exceções e erros de forma controlada
        '''
        self.nome = self.nome
        self.sobrenome = self.sobrenome
        self.celular = self.celular.replace(' ','') # Removendo espaços da string
        self.cpf = self.cpf
    
        super().clean()
        if not all(c.isalpha() or c.isspace() for c in self.nome):
            raise ValidationError('O campo "Nome" deve incluir apenas letras e espaços!')
        
        if not all(c.isalpha() or c.isspace() for c in self.sobrenome):
            raise ValidationError('O campo "Sobrenome" deve incluir apenas letras e espaços!')
        
        if self.idade < 1 or self.idade > 100:
            raise ValidationError('Informe uma idade entre 1 e 100 anos de idade!')
            
        if self.estado == 'E':
            # Nesse caso, caso o valor do atributo seja igual a 'E', isso significa que o cliente não informou um estado, retornando uma mensagem de erro e solicitando que o cliente selecione um estado válido.
            raise ValidationError('Selecione um estado válido!')
        
        if self.cpf:
            ''' Valida CPF '''
            validador = CPF()

            if validador.validate(self.cpf):
                return self.cpf
            
            else:
                raise ValidationError('CPF inválido!')

    @property
    def cpf_formatado(self):
        ''' Formatar o CPF para exibição '''
        return CPF().mask(self.cpf)   
        

    def __str__(self):
        return f'Ficha de Cadastro do(a) Cliente: {self.nome} {self.sobrenome} | CPF: {self.cpf_formatado}'