# Generated by Django 5.0.6 on 2024-06-21 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0003_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='seuemail@rota.com.br', max_length=50),
        ),
    ]