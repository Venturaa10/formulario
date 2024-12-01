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
    '''Formulario de cadastro de Clientes.
    Meta:
        variavie(s):
        - Meta: Modelo referenciado.
        - Exclude: Exclui os campos do modelo que não serão exibidos no formulario.
        - labels: Altera o nome dos campos do modelo, para uma outra exibição no formulario.
        - widgets: Dicionario com os campos a serão exibidos no HTML. Juntamente com o tipo de dado do campo, e seus atributos.
    
    Métodos:
        - init: Método inicializador.
        - _clean_nomeCampo: Validação do campo no formulario.
        
    '''
    class Meta:
        model = Cliente # Este formulario está associada a esse Model

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


    def __init__(self, *args, **kwargs):
        '''
        Argumentos:
            - *args e **kwargs: Permite que nº argumentos sejam passados.
        Atributo:
            - Pega a instancia do objeto, se existir.
        '''
        self.instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)


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

        if Cliente.objects.filter(celular=celular).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('O celular fornecido já está cadastrado para outro cliente.')  

        if not resposta_celular:
            raise forms.ValidationError('Número de celular inválido!')  

        return celular      
        
                    
    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
            
        if estado == 'E':
            raise forms.ValidationError('Selecione um estado válido!')
                
        return estado
            
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Verifica se já existe outro cliente com o mesmo e-mail
        if Cliente.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("O E-mail fornecido já está cadastrado para outro cliente.")
        return email
    

    def clean_cpf(self):
        ''' Validar CPF do formulario.
        Variavei(s):
        - cpf: Pega cpf informado no formulario.

        Validação:
        - Verifica se "cpf" possuí 11 digitos.
        '''
        cpf = self.cleaned_data.get('cpf')
        validador = CPF()

        if Cliente.objects.filter(cpf=cpf).exclude(id=self.instance.id).exists():
            raise forms.ValidationError(f"O CPF fornecido já está cadastrado para outro cliente.")

        if len(cpf) != 11:
            raise forms.ValidationError('O CPF deve conter exatamente 11 dígitos numéricos.')

        if not validador.validate(cpf):
                raise forms.ValidationError('O CPF é inválido!')

        return cpf
    

