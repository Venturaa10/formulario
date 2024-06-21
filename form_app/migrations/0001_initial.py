# Generated by Django 5.0.6 on 2024-06-21 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('sobrenome', models.CharField(max_length=30)),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('telefone', models.CharField(max_length=15)),
                ('comentario', models.TextField(max_length=500)),
            ],
        ),
    ]
