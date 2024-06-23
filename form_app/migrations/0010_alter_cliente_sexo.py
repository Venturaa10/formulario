# Generated by Django 5.0.6 on 2024-06-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0009_alter_cliente_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('I', 'Não Informado'), ('M', 'Masculino'), ('F', 'Feminino')], default='I', max_length=1),
        ),
    ]
