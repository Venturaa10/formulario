# Generated by Django 5.0.6 on 2024-06-30 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0018_alter_cliente_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]