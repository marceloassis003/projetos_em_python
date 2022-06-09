"""
POO - Polimorfismo

poli  -> Muitas
morfis -> Formas

Quando a gente reimplementa um método presente na classe
pai em classes filhas estamos realizando um sobreescrita
de método (Overriding).

O Overriding é a melhor representação do polimorfismo.
"""
class Animal(object):

    def __init__(self, nome):
        self.__nome = nome


    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse metodo')

    def comer(self):
        print(f'{self.__nome} esta comendo... ')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau ')

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau !')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala snif snif..')



# Testando

felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()






















