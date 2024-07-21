# Arquivo responsavél por receber as informações do usuario
from django import forms 
from form_app.models import Cliente

class LoginForm(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True, # Torna o preenchimento desse campo obrigatorio
        max_length= 50,
        widget=forms.TextInput(
            # Estilizando os labels do HTML através do proprio atributo do objeto
            attrs={
                'class': 'form-control', 
                'placeholder': 'Nome Usuario'
            }
        )
    )
    
    senha=forms.CharField(
        label='Senha',
        required=True, # Torna o preenchimento desse campo obrigatorio
        max_length=25,
        widget=forms.PasswordInput(
            # 
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha'
            }
        )
    )

    

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
            'cpf':'CPF', 'comentario': 'Observação'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'Seu nome', 'class':'form-control'}),
            'sobrenome': forms.TextInput(attrs={'placeholder':'Seu sobrenome', 'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-control'}),
            'idade': forms.NumberInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder':'SeuEmail@caminho.com', 'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'placeholder':'11122233399', 'class':'form-control'}),
            'celular': forms.TextInput(attrs={'placeholder':'(00) 11111-1111', 'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'placeholder':'Sugestões', 'class':'form-control'}), 
        }

    # Validações das informações recebidas no template do formulario feita através do metodo "clean_nomeAtributo"

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome.isalpha():
            raise forms.ValidationError('O campo "Nome" não deve incluir números!')
        return nome
        
    def clean_sobrenome(self):
        sobrenome = self.cleaned_data.get('sobrenome')
        if not sobrenome.isalpha():
            raise forms.ValidationError('O campo "Sobrenome" não deve incluir números!')
        return sobrenome
    
    def clean_celular(self):
        celular = self.cleaned_data.get('celular')

        for digito in celular:
            # Para cada digito do número, se esse não for um número inteiro, retorna a mensagem de erro
            if not digito.isdigit():
                raise forms.ValidationError('Número de celular inválido, informe apenas os números sem espaços!')
            
        if len(celular) < 11 or len(celular) > 12 :
            raise forms.ValidationError('Número de celular inválido, informe apenas os números sem espaços!')

        return celular                
                    
    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
            
        if estado == 'E':
            raise forms.ValidationError('Selecione um estado válido!')
                
        return estado
    
    # def clean_cpf(self):
        
            
