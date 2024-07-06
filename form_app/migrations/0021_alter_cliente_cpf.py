# Generated by Django 5.0.6 on 2024-07-06 21:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0020_cliente_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(default='', max_length=11, unique=True, validators=[django.core.validators.RegexValidator('{11}', 'O CPF deve conter exatamente 11 dígitos.')]),
        ),
    ]