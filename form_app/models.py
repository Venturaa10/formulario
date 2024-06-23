# Nesse arquivo é destinado a fazer modificações em admin

from django.db import models
from datetime import datetime # Importação para configurar e trabalhar com data e hora
from django.core.exceptions import ValidationError # Importação para fazer validações
from django.core.validators import MaxValueValidator, MinValueValidator # Importação para validar valores 
# Create your models here.

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

    nome = models.CharField(max_length=20, null=False, blank=False)
    sobrenome = models.CharField(max_length=30, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=OPCAO_SEXO, default='I')
    # 'validators' adicionei parametros para exigir um valor minimo e maximo no campo idade em admin
    idade = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(100)],
        null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=2, choices=OPCAO_ESTADOS_BRASIL, null=False, blank=False, default='E')
    telefone = models.CharField(max_length=15, null=False, blank=False)
    comentario = models.TextField(max_length=500, null=False, blank=False)
    # Atributo que exibe a data e a hora de criação do cliente
    data_criacao = models.DateTimeField(default=datetime.now)
    # Atributo responsavel por indicar se o cliente está ativo ou não
    ativo = models.BooleanField(default=True)

    def clean(self):
        '''
        Metodo responsavél pela realização das validações dos atributos do model Cliente, recomendado para validações simples.
        raise é usado para lidar com exceções e erros de forma controlada
        '''
        super().clean()
        if self.idade < 1 or self.idade > 100:
            raise ValidationError('Informe uma idade entre 1 e 100 anos de idade!')
        
        if self.estado == 'E':
            # Nesse caso, caso o valor do atributo seja igual a 'E', isso significa que o cliente não informou um estado, retornando uma mensagem de erro e solicitando que o cliente selecione um estado válido.
            raise ValidationError('Selecione um estado válido!')

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'