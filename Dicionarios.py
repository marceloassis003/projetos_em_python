"""
DICIONARIOS  - conhecidos por mapas

 - mapeamento entre chave/valor.
 - sao representados pro '{}' print(type({}))
"""

# exemplo 1 - criacao de dicionarios

# forma 1 - (mais comum)

paises = {'br': 'brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# forma 2 - (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

# exemplo 2 - acessando elementos

# forma 1 -  acessando via chave
paises = {'br': 'brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises['br'])
#print(paises['ru'])       #key error

# forma 2 - Acessando via get (recomendado)

print(paises.get('br'))
print(paises.get('ru'))

# caso o get nao encontro o objeto com a chave infromada sera retornado o valor none

pais = paises.get('ru')

if pais:
    print(f'Encontrei o pais {pais}! ')
else:
    print('Nao encontei o pais')
    
# podemos definir um valor padrao, para localizar o objeto    
pais = paises.get('py', 'Nao encontrado')

print(f'Encontrei o pais {pais}! ')
# exemplo 3  - verificando se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# exemplo 4 - podemos ultilizar qualquer tipo de dado

# tuplas podem ser usadas commo chave de dicionarios por serem imutaveis 
localidades = {
    (35.6895, 39.6917): 'Escritorio em Tokio',
    (40.7128, 74.0060): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em São Paulo',

}

print(localidades)
print(type(localidades))
    
# exemplo 5 - adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# forma 1 - Mais comum

receita['abr'] = 350

print(receita)

# forma 2 -

novo_dado = {'maio': 500}

receita.update(novo_dado)       #receita.update({'maio': 500})

print(receita)

# exemplo 6 -  atualizando dados em um dicionario

# forma 1
receita['maio'] = 550

print(receita)

# forma 2
receita.update({'maio': 600})

print(receita)
# exemplo 7 - como remover dados
receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# forma 1 - Mais comum
ret = receita.pop('mar')

print(ret)
print(receita)

# ao remover o objeto o valor dele e sempre retornado

# forma 2 - menos comum
del receita['fev']

print(receita)

# o valor removido não é retornado 
# se a chave nao existir sera gerado erro

# exemplo 8 - aplicaco de dicionarios

# 1 com listas
carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['god of war 4',  1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# teriamos que saber qual e o indice de casa infromaçao no produto

# 2 ultilizando uma tupla

produto1 = ('paystation 4', 1, 2300.00)
produto2 = ('god of war 4',  1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# teriamos que saber qual e o indice de casa infromaçao no produto

# 3 ultilizando dicionario de dados

carrinho = []

produto1 = {'nome': 'playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'god of war 4',  'quantidade': 1,  'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# adicionamos ou removemos produtos no carrinho e em cada produto
# fica mais descritivos as informaçoes dando certeza

# exemplo 9 - metodos de dicionarios
d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# exemplo 1 - limpar o dicionario( zerar dados)
#d.clear()

#print(d)

# exemplo 2  - Copiando um dicionario para outro

# forma 1 - Deep copy
novo = d.copy()

novo['d'] = 4

print(d)
print(novo)

# forma 2 - shallow copy
novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

# exemplo 10 -  forma nao usual de criaçao de dicionarios
outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# o metodo fromkeys recebe dois parametros um iteravel e um valor.
veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)

























