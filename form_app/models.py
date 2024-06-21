from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=20, null=False, blank=False)
    sobrenome = models.CharField(max_length=30, null=False, blank=False)
    # 'validators' adicionei parametros para exigir um valor minimo e maximo no campo idade em admin
    idade = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(105)],
        null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    comentario = models.TextField(max_length=500, null=False, blank=False)


    def __str__(self):
        return self.nome