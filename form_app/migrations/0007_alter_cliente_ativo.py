# Generated by Django 5.0.6 on 2024-06-21 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0006_cliente_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
