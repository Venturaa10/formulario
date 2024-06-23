# Arquivo responsavél por receber as informações do usuario
from django import forms 
from form_app.models import Cliente

class ClienteForm(forms.ModelForm):
    '''Este formulario é baseado no modelo "Cliente" '''
    class Meta:
        model = Cliente # Este formulario está associada a esse Model
        # Lista os campos do modelo a serem exibidos no formulario
        fields = ['nome', 'sobrenome', 'sexo', 'idade', 'email', 'estado', 'telefone', 'comentario','ativo']
        ''' widgets
        -> Define como cada campo será renderizado / exibido no HTML
        -> "forms.atributo" são widgets do Django que controlam a aparência e comportamento dos campos.
        -> Parametro 'disabled': Faz com que não seja possivel alterar o status de "ativo" diretamente, ou seja, a alteração só pode ser feito no banco de dados
        '''
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome'}),
            'sobrenome': forms.TextInput(attrs={'placeholder': 'Seu sobrenome'}),
            'sexo': forms.Select(),
            'idade': forms.NumberInput(),
            'estado': forms.Select(),
            'email': forms.EmailInput(attrs={'placeholder': 'SeuEmail@caminho.com'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(00) 11111-1111'}),
            'comentario': forms.Textarea(attrs={'placeholder': 'Sugestões'}),
            'ativo': forms.CheckboxInput(attrs={'disabled': 'disabled'}), 
        }
