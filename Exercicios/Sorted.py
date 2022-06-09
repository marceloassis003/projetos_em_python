"""
Sorted

Obs: apesar do nome, com a funçao sort() que ja estudamos em listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer iteravel.

Como o proprio nome diz. Sorted() serve para ordenar.

obs: o sorted() sempre retorna uma lista com os elemntos do iteravel ordenados

# exemplo

numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros)) # ordenar do menor para o maior

print(numeros)


numeros = [6, 1, 8, 2]
print(numeros)

print(tuple(sorted(numeros)))
# adiconando parametros ao sorted()

print(sorted(numeros, reverse=True))    # ordena do maior para o menor

# podemos ultlizar o sorted() para coisas mais complexas

usuarios = [
    {"username:": "Samuel", "tweets": ['Eu amo bolos', 'Eu amo salgados']},
    {"username:": "Carla", "tweets": ['Eu amo meu gato']},
    {"username:": "ester", "tweets": []},
    {"username:": "Jesse", "tweets": [], "cor": "amarelo"},
    {"username:": "Caio666", "tweets": ['Eu amo cachorros', 'vou sair']},
    {"username:": "Gabi", "tweets": [], "cor": "Preto", "musica": "rock"}
]

print(usuarios)

# Ordenando por username - Ordem Alfabetica
print(sorted(usuarios, key=lambda usuario: usuario["username:"], reverse=True))

#  Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))



"""
# ultimo exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "on", "tocou": 2},
    {"titulo": "how like that", "tocou": 4},
    {"titulo": "tundler", "tocou": 32}

]

# Ordena de menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))

print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))































