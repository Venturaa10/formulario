# Arquivo responsavél por receber as informações do usuario
from django import forms 
from form_app.models import Cliente
from validate_docbr import CPF, CNPJ
import re


class LoginForm(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True, # Torna o preenchimento desse campo obrigatorio
        max_length= 50,
        widget=forms.TextInput(
            # Estiliza os labels do HTML através do proprio atributo do objeto
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
        - Define como cada campo será renderizado / exibido no HTML
        - "forms.atributo" são widgets do Django que controlam a aparência e comportamento dos campos.
        - Parametro 'disabled': Faz com que não seja possivel alterar o status de "ativo" diretamente, ou seja, a alteração só pode ser feito no banco de dados
        '''
        exclude = ['data_criacao','status']

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
        ''' Validar nome informado no formulario.
        - A função "all" -> Retorna "True" se todos os elementos do iterável fornecido forem "True".
        
        - c.isalpha() -> Retorna "True" se "c" for uma letra, ou seja, Números e/ou caracteres especiais é "False".
        
        - c.isspace() -> Retorna "True" se "c" for um espaço, permitindo nome compostos como: "Lucas Miguel"
        
        - Importante! Essa lógica deve ser implementada tanto em "forms" quanto em "models" para funcionar corretamente na interface HTML.
        '''
    
        nome = self.cleaned_data.get('nome')
        if not all(c.isalpha() or c.isspace() for c in nome):
            raise forms.ValidationError('O campo "Nome" deve incluir apenas letras!')
        return nome
        
    def clean_sobrenome(self):
        sobrenome = self.cleaned_data.get('sobrenome')
        if not all(c.isalpha() or c.isspace() for c in sobrenome):
            raise forms.ValidationError('O campo "Sobrenome" deve incluir apenas letras!')
        return sobrenome
    
    def clean_celular(self):
        celular = self.cleaned_data.get('celular').replace(' ', '')
        regex_celular =  r'^[0-9]{2,3}[0-9]{5}[0-9]{4}$'
        resposta_celular = re.findall(regex_celular,celular) # Busca modelo na variavel celular.
        if resposta_celular:
            return celular      
        else:
            raise forms.ValidationError('Número de celular inválido!')  
        
                    
    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
            
        if estado == 'E':
            raise forms.ValidationError('Selecione um estado válido!')
                
        return estado
            
    def clean_cpf(self):
        ''' Validar CPF do formulario.
        Variavei(s)}:
        - cpf: Pega cpf informado no formulario.

        Validação:
        - Verifica se "cpf" possuí 11 digitos.

        '''
        cpf = self.cleaned_data.get('cpf')

        if len(cpf) == 11:
            validador = CPF()
            if validador.validate(cpf):
                return cpf
            else:
                raise forms.ValidationError('CPF Inválido!')
        
        else:
            raise forms.ValidationError('O CPF deve conter exatamente 11 dígitos numéricos.')

