# Generated by Django 5.0.6 on 2024-06-21 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0002_alter_cliente_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='seuemail@rota.com.br', max_length=30),
        ),
    ]
