from rest_framework import serializers
from django.contrib.auth import authenticate

#classe serializer para o login
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    #função pra validar as informações
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        #tentativa de autenticação
        user = authenticate(username=username, password=password)

        #caso falhe, mostre o erro de validação
        if not user:
            raise serializers.ValidationError('Credenciais inválidas')

        #se der certo, vai pros atributos
        attrs['user'] = user
        return attrs
    
    #o serializer foi criado pra poder usar o api
