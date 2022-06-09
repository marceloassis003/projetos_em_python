"""
CONJUNTOS ->

 - estamos fazendo referencia a "teoria dos conjuntos da matematica"
 - conjuntos em python sao chamados de 'Sets'
     - Sets sao referenciados com '{}'
     - Sets nao possuem valores duplicados
     - Sets nao possuem valores ordenados
     - conjuntos nao sao indexados

* conjuntos sao necessarios, quando precisamos armazenar elementos mas nao nos importamos com a ordenação.
* ultlizamos quando nao precisamos nos preocupar com chaves, valores e itens duplicados.

"""

# exemplo 1 - definindo um conjunto
# forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})     # possui valores repetidos

print(s)
print(type(s))

# ao criar um conjunto caso seja adicionado um valor ja existente, o mesmo sera ignorado.

# forma 2

s = {1, 2, 3, 4, 5, 5}

print(s)
print(type(s))
# exemplo 2 - verificando se o elemento esta contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('nao tem o 3')
# exemplo 3 - nao temos uma ordem

# listas aceitam valores duplicados
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista: {lista} com {len(lista)} elementos')

# tuplas aceitam valore duplicados
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos ')

# dicionarios nao aceitam chaves duplicados
dicionario = {}.fromkeys(lista,'dict')
print(f'dicionario: {dicionario} com {len(dicionario)} elementos')

# conjuntos nao aceitam valores duplicados
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')
# exemplo 4 - tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}

print(s)
print(type(s))

# exemplo 5 - iterando com o Set
for valor in s:
    print(valor)
# exemplo 6 - usos interresantes com o set

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# precisamos saber quantas cidades unicas temos

print(len(set(cidades)))
# exemplo 6 - adicionando elementos em um conjunto
s = {1, 2, 3, 4}

s.add(4)
s.add(4)    # duolicidade nao gera erro (sera ignorado)
print(s)

# exemplo 7 - remover elemtos de um conjunto
s = {1, 2, 3}
print(s)

# forma 1
s.remove(3)     # devemos informar o valor a ser removido

print(s)

# forma 2
s.discard(2)
s.discard(22)        # para valores nao encontrado nao sera gerado erro

print(s)
# exemplo 8 - copiando um conjunto para outro
s = {1, 2, 3}

print(s)

#    fomra 1 - Deep copy
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

#   forma 2  - shallow copy
novo = s

novo.add(4)

print(novo)
print(s)
# exemplo 9 - removendo todos os itens do conjunto
s = {1, 2, 3}
print(s)

s.clear()
print(s)
# exemplo 10 - metodos matematicos de conjuntos

estudantes_phyton = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# conjunto com nomes de estudantea unicos

# forma 1 - ultilizando union

unicos1 = estudantes_phyton.union(estudantes_java)
print(unicos1)

# forma 2 - ultilizando o caractere '|'

unicos2 = estudantes_phyton | estudantes_java

print(unicos2)

# gerar um conjunto de estudantes que estao em ambos os curso

# forma 1 - ultilizando intersection

ambos1 = estudantes_phyton.intersection(estudantes_java)
print(ambos1)

# froma 2 - ultilizando o caractere '&'

ambos2 = estudantes_phyton & estudantes_java
print(ambos2)

# gerar um conjunto de estudantes de um curso que nao estao no outro

so_python = estudantes_phyton.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_phyton)
print(so_java) 



# exemplo 11 - soma*, valor maximo*, valor minimo*, tamanho
s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))









