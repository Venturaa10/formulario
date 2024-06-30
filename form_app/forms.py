# Arquivo responsavél por receber as informações do usuario
from django import forms 
from form_app.models import Cliente

class ClienteForm(forms.ModelForm):
    '''Este formulario é baseado no modelo "Cliente" '''
    class Meta:
        model = Cliente # Este formulario está associada a esse Model
        ''' widgets
        -> Define como cada campo será renderizado / exibido no HTML
        -> "forms.atributo" são widgets do Django que controlam a aparência e comportamento dos campos.
        -> Parametro 'disabled': Faz com que não seja possivel alterar o status de "ativo" diretamente, ou seja, a alteração só pode ser feito no banco de dados
        '''
        exclude = ['data_criacao','ativo']

        labels = {
            'comentario': 'Comentário'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'Seu nome', 'class':'form-control'}),
            'sobrenome': forms.TextInput(attrs={'placeholder':'Seu sobrenome', 'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-control'}),
            'idade': forms.NumberInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder':'SeuEmail@caminho.com', 'class':'form-control'}),
            'telefone': forms.TextInput(attrs={'placeholder':'(00) 11111-1111', 'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'placeholder':'Sugestões', 'class':'form-control'}), 
        }

        '''As validações abaixos estão funcionando, porém a mensagem não está sendo exibida no template'''
    # def clean_telefone(self):
    #     telefone = self.cleaned_data.get('telefone')

    #     if len(telefone) < 15:
    #         raise forms.ValidationError('Número de telefone invalido, talvez esteja faltando digitos!')

    #     else:
    #         return telefone
            
                
    # def clean_estado(self):
    #     estado = self.cleaned_data.get('estado')

    #     if estado == 'E':
    #         raise forms.ValidationError('Selecione um estado válido!')
            
    #     else:
    #         return estado