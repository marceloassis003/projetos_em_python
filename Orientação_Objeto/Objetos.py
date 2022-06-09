"""
POO - Objetos

objetos -> São instancias da classe, ou seja, após o mapeamento do objeto do mundo real para
sua representação computacional, devemos poder criar quantos objetos forem necessarios. Podemos
pensar nos objetos/instancias de uma classe como variaveis do tipo definido na classe.


# Instancias/Objetos

lamp1 = Lampada('Branca', 110, 60)

lamp1.on_off()


print(f'A lampada está ligada ? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 20000)

user1 = Usuario('Felicity', 'Jones', 'feliciti@gmail.com', '123456')


nome = 'Angelina'
sobrenome = 'Jolie'
email = 'angelina@gmail.com'
senha = '123456'

user = Usuario(nome, sobrenome, email, senha)

print(type('Geek'))

print(type(42))

print(type(user))
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def on_off(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome} diz OI ')

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


class Usuario:

    contador = 0

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        Usuario.contador = self.__id



cli1 = Cliente('Angelina', '123.456.789-99')

cc = ContaCorrente(5000, 20000, cli1)

cc.mostra_cliente()

cc._ContaCorrente__cliente.diz()




























