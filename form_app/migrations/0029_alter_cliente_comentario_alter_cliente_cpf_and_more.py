# Generated by Django 5.0.6 on 2024-07-06 23:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0028_alter_cliente_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='comentario',
            field=models.TextField(blank=True, help_text='Uma sugestão aqui :)', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(default='', help_text='11122233399', max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{11}$', 'O "CPF" deve conter exatamente 11 dígitos apenas!')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(help_text='emailCliente@dominio.com', max_length=50, unique=True, validators=[django.core.validators.EmailValidator(message='Email fornecido é inválido!')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(help_text='Nome do Cliente', max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(help_text='Sobrenome do Cliente', max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(help_text='11 92111-3212', max_length=12, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{2,3} ?[9][0-9]{4}-?[0-9]{4}$', 'O "número" fornecido é inválido, formato recomendado: 21 912345678!')]),
        ),
    ]
