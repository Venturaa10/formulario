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
            'cpf':'CPF', 'comentario': 'Comentário'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'Seu nome', 'class':'form-control'}),
            'sobrenome': forms.TextInput(attrs={'placeholder':'Seu sobrenome', 'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-control'}),
            'idade': forms.NumberInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder':'SeuEmail@caminho.com', 'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'placeholder':'111.222-333-45', 'class':'form-control'}),
            'telefone': forms.TextInput(attrs={'placeholder':'(00) 11111-1111', 'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'placeholder':'Sugestões', 'class':'form-control'}), 
        }

    '''
    Validações das informações recebidas no template do formulario feita através do metodo "clean_nomeAtributo"
    '''

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')

        for digito in telefone:
            # Para cada digito do número, se esse não for um número inteiro, retorna a mensagem de erro
            if not digito.isdigit():
                raise forms.ValidationError('O número de telefone deve ser compostor somente por números inteiros!')
            
        if len(telefone) < 11 or len(telefone) >= 13 :
            raise forms.ValidationError('Número de telefone inválido!')

        return telefone                
                    
    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
            
        if estado == 'E':
            raise forms.ValidationError('Selecione um estado válido!')
                
        return estado
    
    # def clean_cpf(self):
        
            
