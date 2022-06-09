"""
Any e All

all() -> Retorna True se todos os elementos do iteravel são verdadeiros  ou ainda se o iteravel esta vazio.

# exemplo all()

print(all([0, 1, 2, 3, 4])) # todos os numeros são verdadeiros? R: False

print(all([1, 2, 3, 4])) # todos os numeros são verdadeiros? R: True

print(all([])) # todos os numeros são verdadeiros? R: True

print(all((1, 2, 3, 4))) # todos os numeros são verdadeiros? R: True

print(all({1, 2, 3, 4})) # todos os numeros são verdadeiros? R: True

print(all(('Geek'))) # todos os numeros são verdadeiros? R: True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Crisitna ']

print(all([nome[0] == 'C' for nome in nomes]))

# obs: um iteravel vazio convertido em boolean é False, mas o all() entende como True
print(all(letra for letra in 'eio' if letra in 'aeiou'))

print(all(num for num in [4, 2, 10, 6, 8] if num % 2 == 0))

- any() -> retorna True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vazio, retorna False
"""

print(any([0, 1, 2, 3, 4]))     # True

print(any([0, False, {}, {}, []]))     # False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Crisitna ', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))

















