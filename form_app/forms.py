# Arquivo responsavél por receber as informações do usuario
from django import forms 
from form_app.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'sexo', 'idade', 'email', 'estado',  'telefone', 'comentario','ativo']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome'}),
            'sobrenome': forms.TextInput(attrs={'placeholder': 'Seu sobrenome'}),
            'sexo': forms.Select(),
            'idade': forms.NumberInput(),
            'estado': forms.Select(),
            'email': forms.EmailInput(attrs={'placeholder': 'SeuEmail@caminho.com'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(00) 11111-1111'}),
            'comentario': forms.Textarea(attrs={'placeholder': 'Sugestões'}),
            'ativo': forms.CheckboxInput(),
        }

