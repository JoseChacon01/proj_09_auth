from django.db import models

from django.contrib.auth.models import AbstractUser #Padrão

class Usuario(AbstractUser):# Vai conter no BD, uma sequecia de colunas padrão + os campos criados abaixo.
    nome = models.CharField('Nome', max_length=100)
    idade = models.IntegerField('Idade')
    cpf = models.CharField('CPF', max_length=11, unique=True) #unique não permite que tenha 2 cadastros com o memso dado, nesse caso, o CPF.

    USERNAME_FIELD = 'cpf' #A partir de agora o usuario deverá logar com o CPF, e não mais com o usuario.

    class Meta:
        permissions = [ #Acrescentando 2 novas permissões na lista de permissões do usuario no Banco de Dados.
            ('permissao_01', 'Permite acessar a view Teste'),
            ('permissao_02', 'Permite visualizar um botão na página')
        ]

