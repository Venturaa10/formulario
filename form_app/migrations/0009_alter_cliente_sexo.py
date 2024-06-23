# Generated by Django 5.0.6 on 2024-06-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0008_cliente_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('O', 'Outro'), ('M', 'Masculino'), ('F', 'Feminino')], default='O', max_length=1),
        ),
    ]
