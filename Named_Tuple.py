"""
Modulo Collections -> Named Tuple

# recap tupla
tupla = {1, 2, 3}

print(tupla[1])

Named Tuple -> São tupla, diferenciados, onde, especificamos um nome para a mesma e parametros.
"""
# realizando o import
from collections import namedtuple

# definindo o nome e parametros.

# forma 1
cachorro = namedtuple('cachorro', 'idade raca nome')



# forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# usando
ray = cachorro(idade=2, raca='chow-chow', nome='Ray')

print(ray)
# acessando os dados

# forma 1

print(ray[0])   #  idade
print(ray[1])   # raca
print(ray[2])   # nome

# forma 2
print(ray.idade)    #  idade
print(ray.raca)     # raca
print(ray.nome)     # nome

print(ray.index('chow-chow'))

print(ray.count('chow-chow'))









