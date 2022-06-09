"""
Min e Max

max() -> retorna o maior valor em um iteravel ou o maior de 2 ou mais elemento.

# exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))       # 129

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))       # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))       # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))       # 129

# faça um programa que receba dois valores do usuario e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))


print(max(4, 67, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(3.145, 5.789))

print(max('Geek University'))

min() -> retorna o menor item ou menor valor em um iteravel ou o menor de dois ou mais elemntos

# exemplos min

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))       # 129

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))       # 129

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))       # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))       # 129

# faça um programa que receba dois valores do usuario e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1, val2))


print(min(4, 67, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(3.145, 5.789))

print(min('Geek University'))

# outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivander']

print(max(nomes))   # Tim

print(min(nomes))   # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Olivander

print(min(nomes, key=lambda nome: len(nome)))   # Tim

"""

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "on", "tocou": 2},
    {"titulo": "how like that", "tocou": 4},
    {"titulo": "tundler", "tocou": 32}

]

print(max(musicas, key=lambda musica: musica["tocou"]))
print(min(musicas, key=lambda musica: musica["tocou"]))

# DESAFIO! Imprima somente o titulo da musica mais e menos tocada
print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])
print(min(musicas, key=lambda musica: musica["tocou"])["titulo"])

# DESAFIO ! Como encontrar a musica mais tocada e a menos sem usar max(), min() e lambda ?

# musica mais tocada
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

    elif musica['tocou'] == max:
        print(musica['titulo'])


# musica menos tocada
min = 999999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

    elif musica['tocou'] == min:
        print(musica['titulo'])























































