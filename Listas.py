"""
Lista phyton funcional
difernça de serem DINAMICOS e tambem poder colocar QUALQUER tipo de dado.

- Dinamico: nao possui tamanho fixo; podemos criar a lista e ir adicionando elementos;

"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', '', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 46464546749]

cores = ['verde', 'amarelo', 'azul', 'branco']


#exemplo 1 - verificando valor na lista
num = 7

if num in lista4:
    print(f'Ecnontrei o numero {num}')
else:
    print(f'Nao encontrei o numero {num}')

# exemplo 2 - ordenando uma lista
lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

# exemplo 3 - contar numero de ocorrencias de um alista
print(lista1.count(1))
print(lista5.count('e'))

# exemplo 4 - adiconar elemntos em listas
print(lista1)
lista1.append(42)
print(lista1)

# lista1.append(12, 34, 56) #erro so 1 elemento por vez

lista1.append([22, 27, 27]) # coloca um tipo de dado lista
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Nao encontrei a lista')

lista1.extend([123, 44, 67]) # cada elemento como valor adicional
print(lista1)
# exemplo 5 - inserindo elemnto na lista informando a posicao
lista1.insert(2, 'novo valor')
print(lista1)

# exemplo 6 - juntando 2 listas
lista1 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

# exemplo 7 - invertendo uma lista
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

print(lista1[::-1])
print(lista2[::-1])
# exemplo 8 - copiando uma lista
lista6 = lista2.copy()
print(lista6)

# exemplo 9 - contando elemntos da lista
print(len(lista1))

# exemplo 10 - remover ultimo elemnto da lista
print(lista5)
lista5.pop()
print(lista5)

lista5.pop(2)  #removendo pela posicao da lista 
print(lista5)

# exemplo 11 - removendo todos elementos da lista
print(lista5)
lista5.clear()
print(lista5)

# exemplo 12 - repetindo elementos da lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# exemplo 13 - converter string para lista

# exemplo 1
curso = 'programacao em phyton essencial'
print(curso)
curso = curso.split()           # separa pelo espaço entre elas
print(curso)

#exemplo 2
curso = 'programacao, em, phyton, essencial'
print(curso)
curso = curso.split(',')
print(curso)

# exemplo 14 - convertendo uma lista em uma string
lista6 = ['programcao', 'em', 'python', 'essencial']
print(lista6)

curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)

# exemplo 15 - qualuqer tipo de dado na lista
print(lista6)
print(type(lista6))

# exemplo 16 - iterando sobre listas
# exemplo 1 - ultilizando for
soma = None

for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# exemplo 2 - ultilizando while
carrinho = []
produto = ''

while produto != 's':
    print("adicione um produto na lista ou digite 's' para sair: ")
    produto = input()
    if produto != 's':
        carrinho.append(produto)
    


for produto in carrinho:
    print(produto)
# exemplo 17 - ultilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)
# exemplo 18 - acesso aos elementos em forma indxada
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# acesso forma indexada inversa
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])
# exemplo 19 - loop com lista

for cor in cores:
    print(cor)

indice = 0

while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
# exemplo 20 - gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)
# exemplo  21 - listas aceitam valores repetidos
lista = []

lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)
# exemplo 22 - outros metodos de lista

# exemplo 1 - encontrar indice de um elemento
numeros = [5, 6, 7, 5, 8, 9, 10]

print(numeros.index(6))

print(numeros.index(9))

print(numeros.index(5))

print(numeros.index(5, 1))

print(numeros.index(8, 3, 6))
# exemplo 23 - revisao de slicing

#lista = [inicio:fim:passo]
#range = (inicio:fim:passo)

# exemplo 1 - slice parametro inicio
lista = [1, 2, 3, 4]

print(lista[1:])

# exemplo 2 - slice parametro fim
print(lista[:2])

print(lista[:4])

print(lista[1:3])

# exemplo 3 - slice parametro passo
print(lista[1::2])

print(lista[::2])
# exemplo 24 - invertendo valores de uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes.reverse()

print(nomes)
# exemplo 25 - soma*, valor maximo*, valor minimo*, tamanho
lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))   # soma
print(max(lista))   # valor maximo
print(min(lista))   # valor minimo
print(len(lista))   # tamanho da lista
# exemplo 26 - transformando uma lista em tupa
lista = [1, 2, 3, 4, 5, 6]

print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))
# exemplo 27 - Desempacotamento de listas
lista = [1, 2, 3, 4]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# emeplo 28 - copiando de uma lista para outra (shallow copy e deep copy)
# exemplo 1 - deep copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# exemplo 2 - shallow coppy
lista = [1, 2, 3]
print(lista)

nova = lista

print(nova)
nova.append(4)

print(lista)
print(nova)

































