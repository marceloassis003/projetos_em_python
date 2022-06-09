"""
POO - Herança Multipla

Herança Multipla nada mais é do que a possiilidade de uma classe herdar
de multiplas classes,  fezando com que as classes filhas herdes todaos os
atributos e metodos de todas as classe herdadas.

OBS: A herança multipla pode ser feitas de duas maneiras:
    - Por multiderivação direta;
    - Por multiderivação indireta;


# Exemplo 1 - Multiderivaçãi direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class Multiderivada(Base1, Base2, Base3):
    pass

# Exemplo 2 - Multiderivação indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass


OBS: Não importa se a derivção é direta ou indireta. A classe que realizar a
herança herdara todos os atributos e metodos da super classes.


"""
class Animal:

    def __init__(self, nome ):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'eu sou {self._Animal__nome} do mar !'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra !'

class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)



# TEstando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Shin')
print(tatu.andar())
print(tatu.cumprimentar())

Tux = Pinguim('tux')
print(Tux.andar())
print(Tux.nadar())
print(Tux.cumprimentar())   # Mehod Resolution Order - MRO

# Objeto é a unica instancia de....

print(f'Tux é instancia de Pingum? {isinstance(Tux, Pinguim)}')          # True
print(f'Tux é instancia de Aquatico? {isinstance(Tux, Aquatico)}')      # True
print(f'Tux é instancia de Terrestre? {isinstance(Tux, Terrestre)}')    # True
print(f'Tux é instancia de animal? {isinstance(Tux, Animal)}')          # True
print(f'Tux é instancia de object? {isinstance(Tux, object)}')           # True

























































































