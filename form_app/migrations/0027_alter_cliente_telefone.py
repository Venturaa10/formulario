# Generated by Django 5.0.6 on 2024-07-06 22:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0026_alter_cliente_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{2,3} ?[0-9]{5}-?[0-9]{4}$', 'O "número" fornecido é inválido!')]),
        ),
    ]
