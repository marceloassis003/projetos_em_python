"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico
ultlizando classes.

Encapsular -> cápsula


    classe
---------------------------------
|                               |
|       atributos e métodos     |
|_______________________________|

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método priado
chamado __falar

Esses elementos privados só devem/deviriam ser acessados
dentro da classe. Mas python não bloqueia este acesso
fora da classe. Com python acontece um fenomeno chamado
Name Mangling, que faz uma alteração na forma de se
acessar os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elemtos privados fora da classe:

instancia._Pessoa.__nome

instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de um classe,
escondendo atributos e métodos privados de usuário.


# Testando

print(conta1.__dict__)

conta1.extrato()

print(conta1._Conta__titular)       # Name Mangling

conta1._Conta__titular = 'Angelina'

print(conta1.__dict__)


print(conta1.__dict__)

conta1.depositar(150)

print(conta1.__dict__)

conta1.sacar(200)

print(conta1.__dict__)


conta1 = Conta('Angelina ', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Felicity', 300, 2000)
conta2.extrato()

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()
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
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

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
                print('Saldo Insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  #  taxa de transferencia paga por quem realizou a transferência

        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor




































































































