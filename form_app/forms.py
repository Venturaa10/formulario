# Arquivo responsavél por receber as informações do usuario
from django import forms 

class CadastroUser(forms.Form):
    nome_user = forms.CharField(
        # Parametros aqui
        label='Nome de Usuario',
        required=True,
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Seu nome',
                'class': 'form-control',
                   }
        )

    )

    sobrenome_user = forms.CharField(
        # Parametros aqui
        label='Sobrenome',
        required=True,
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Seu nome',
                'class': 'form-control',
                   }
        )
    )

    email_user = forms.EmailField(
        label='Email',
        required=True, # Torna o preenchimento desse campo obrigatorio
        max_length= 100,
        widget=forms.EmailInput(
            # Estilizando os labels do HTML através do proprio atributo do objeto
            attrs={
                'class': 'form-control', 
                'placeholder': 'seuemail@tipo.com'
            }
        )
    )

    comentario_user = forms.CharField(
        label='Comentario',
        required=True, # Torna o preenchimento desse campo obrigatorio
        max_length= 500,
        widget=forms.TextInput(
            # Estilizando os labels do HTML através do proprio atributo do objeto
            attrs={
                'class': 'form-control', 
                'placeholder': 'Deixe um comentario'
            }
        )
    )