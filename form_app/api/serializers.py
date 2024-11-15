from rest_framework import serializers
from form_app.models import Cliente
from form_app.api.validators import * # Importa as validações

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, dados):
        '''Método responsavel por realizar as validações dos campos do estudante'''
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só deve conter letras!'})
         
        if sobrenome_invalido(dados['sobrenome']):
            raise serializers.ValidationError({'sobrenome':'O sobrenome só deve conter letras!'})

        if email_invalido(dados['email']):
            raise serializers.ValidationError({'email': 'O email deve ser valido!'})
        
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O campo CPF deve ter um valor valido!'})
        
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular':'O campo celular precisa seguir um modelo parecido com: 11900000000 (DDD + número sem espaços ou caracteres especiais).'})

        return dados
      