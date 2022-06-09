"""
POO - Herança (Inheritance)

Ideia de herança é a de reaproveitar codigo. Tambem extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

Perguntar: Existe alguma entidade  genérica o sufucuente para encapsular
os atributos e métodos comuns e outras entidades ?


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Angelina', 'Jolie', '123,456.789-00', 5000)
funcionario1 = Funcionario('felicity', 'Jones', '987.654.321-11', 1234)


print(cliente1.nome_completo())
print(funcionario1.nome_completo())

OBS: Quando uma classe herda de uma classe, ela herda todos os atributos e
métodos da classe herdade (Pai).

Quando uma classe herda de outras classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - CLasse Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Especifica;


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    #   Cliente herda de Pessoa

    def __init__(self,nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # forma não comum de acessar dados da superclasse
        self.__renda = renda


class Funcionario(Pessoa):
    #   Funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da superclasse
        self.__matricula = matricula






cliente1 = Cliente('Angelina', 'Jolie', '123,456.789-00', 5000)
funcionario1 = Funcionario('felicity', 'Jones', '987.654.321-11', 1234)


print(cliente1.nome_completo())
print(funcionario1.nome_completo())



print(cliente1.__dict__)
print(funcionario1.__dict__)

# Sobrescrita de Métodos (Overriding)

Sobreescrita de método ocorre quando reescrevemos/reeimplementamos um método presete
na super classe em uma classe ou em classes filhas.

"""

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self,nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # forma não comum de acessar dados da superclasse
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da superclasse
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionario: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Angelina', 'Jolie', '123,456.789-00', 5000)
funcionario1 = Funcionario('felicity', 'Jones', '987.654.321-11', 1234)



print(cliente1.nome_completo())
print(funcionario1.nome_completo())
































