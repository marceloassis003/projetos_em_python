"""
Filter

filter() -> filtrar dados de uma determinada coleçao.

# exemplo media
valores = (1, 2, 3, 4, 5, 6)

media = (sum(valores) / len(valores))

print(media)

# biblioteca para trabalhar com dados estatisticos
import statistics

# dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# calculando a média dos dados ultilizando a funçao mean()

media = statistics.mean(dados)

print(f'Media: {media}')
# obs: assim como a funçao map(), a filter() recebe dois paramentros, sendo
# uma funçao e um iteravel.

res = filter(lambda x: x > media, dados)
print(list(res))

# obs: assim como na funçao map(), apos serem ultilizados os dados de filter() eles sao excluidos da memória.
#   print(f'Novamente: {list(res)}')


# exemplo 2
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Clombia', '', 'Equador', '',  '', 'Venezuela']

print(paises)

#res = filter(lambda x: x != '', paises) # minha maneira
# res = filter(lambda pais: len(pais) > 0, paises)
res = filter(None, paises)


print(list(res))

# A diferença entre map() e filter() é:

# map() recebe 2 parametros, uma funçao e um iteravel e retorna um objeto baseando a funçao para cada elemento do iteravel

# filter() recebe dois parametros, uma funçao e um iteravel e retorna um objeto filtrando apenas os elementos de acordo com a


# exemplo mais complexo

usuarios = [
    {"username:": "Samuel", "tweets": ['Eu amo bolos', 'Eu amo salgados']},
    {"username:": "Carla", "tweets": ['Eu amo meu gato']},
    {"username:": "ester", "tweets": []},
    {"username:": "Jesse", "tweets": []},
    {"username:": "Caio666", "tweets": ['Eu amo cachorros', 'vou sair']},
    {"username:": "Gabi", "tweets": []}
]

print(usuarios)
# filtrar os usuarios que estao inativos no Twitter

# forma 1
inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))
print(inativos)

# forma 2

inativos = list(filter(lambda user: not user['tweets'], usuarios))
print(inativos)

"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua intruttora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)






















