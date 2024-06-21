# Arquivo responsavél por receber as informações do usuario
from django import forms 

class CadastroUser(forms.Form):
    nome_user = forms.CharField(
        # Parametros aqui
        label='Nome de Usuario',
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Seu nome',
                'class': 'form-control',
                   }
        )

    )
