# Nesse arquivo é destinado a fazer modificações em admin

from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Cliente(models.Model):
    OPCAO_SEXO = [
        ('I', 'Não Informado'),
        ('M', 'Masculino'), 
        ('F', 'Feminino'),
    ]

    nome = models.CharField(max_length=20, null=False, blank=False)
    sobrenome = models.CharField(max_length=30, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=OPCAO_SEXO, default='I')
    # 'validators' adicionei parametros para exigir um valor minimo e maximo no campo idade em admin
    idade = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(105)],
        null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    comentario = models.TextField(max_length=500, null=False, blank=False)
    # Atributo que exibe a data e a hora de criação do cliente
    data_criacao = models.DateTimeField(default=datetime.now)
    # Atributo responsavel por indicar se o cliente está ativo ou não
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'