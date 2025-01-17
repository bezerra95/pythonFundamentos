﻿"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico hierárquico utilizando
classes.

Encapsular -> cápsula


               Classe
----------------------------------
|                                |
|      atributos e métodos       |
|                                |
__________________________________

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método privado
chamado __falar()

Esses elementos privados devem/deveriam ser acessados
dentro de uma classe. Mas Python não bloqueia este acesso
fora da classe. Com Python acontece um fenômeno chamado
Name Mangling, que faz uma alteração na forma de se
acessar os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instância._Pessoa__nome

instância._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.


"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de transferência paga por quem realizou a transferência

        # 2 - Adicionar o valor na conta destino
        conta_destino.__saldo += valor


# Testando

conta1 = Conta('Julio Cesar', 3_000, 6_000)
conta1.extrato()
print()
conta2 = Conta('Abigail', 9_000, 12_000)
conta2.extrato()
print()
conta2.transferir(100, conta1)

conta1.extrato()
print()
conta2.extrato()

