"""
MAPAS  -> conhecidos em python como dicionarios

dicionarios em python sao representados por '{}'

"""


# exemplo 1  - como iterar com dicionarios
receita = {'jan': 100, 'fev': 250, 'mar': 400}

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# exemplo 2 - acessando as chaves
print(receita.keys())

 
for chave in receita.keys():
    print(receita[chave])
    
# exemlo 3 - acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

# exemplo 4 - desempacotamento de dicionarios
print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# exemplo 5 - soma*, valor maximo*, valor minimo*, tamanho*
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))










