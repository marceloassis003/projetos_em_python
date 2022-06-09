"""
Dictionary Comprehension

pense no seguinte:

Se quisemos criar uma lista fazemos:

lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:

tupla = {1, 2, 3, 4}  # 1, 2, 3, 4

Se quisermo criar um set (conjunto)

conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionario:

dicionario = {'a: 1, 'b': 2, 'c': 3, 'd': 4}

# sintax

{chave: valor  for valor in iteravel}

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado ={chave : valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

# 2

numeros = [1, 2, 3, 4, 5, 1, 2]

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)


# 3

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}

print(mistura)


# 4  Exemplo com logica condicional

numeros = [1, 2, 3, 4, 5]

res = {n: ('par' if n % 2 == 0 else 'impar') for n in numeros}

print(res)

"""

















