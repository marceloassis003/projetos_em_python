"""
Reversed

Obs: nao confunda com a função reverse() que estudamos nas Listas.

A função reverse() so funciona em listas.

Já a função reversed() funciona com qualquer iteravel.

Sua função é inverter o iteravel.

A função reversed() retorna um iteravel chamado List Reverse Iterator
"""
# exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# podemos converter o elemento reornado para uma lista, Tupla ou conjunto

# lista
print(list(reversed(lista)))

# tupla
print(tuple(reversed(lista)))

# OBS: Em conjuntos, não definimos a ordem dos elemntos
# conunto (SET)
print(set(reversed(lista)))

# podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')
# podemos fazer o memso sem o uso do for
print(''.join(list(reversed('Geek University'))))

# ja vimos como fazer isso mais facil com o slice de strings
print('Geek University'[::-1])

# Podemos tambem ultlizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

# Apesar que tambem ja vimos como fazer isso ultlizando o proprio range()
for n in range(9, -1, -1):
    print(n)



























