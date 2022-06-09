"""
Listas Aninhadas ( Nested Lists)

- Algumas linguagens de programaçao possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (arrays/vetores);
    -Multidimensionais (Matrizes);

Em python nos temos as listas

numeros = [1, ''b, 3.241, True, 5]

# exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]      # Matriz  3 x 3

print(listas)
print(type(listas))

# como fazemos para acessar os dados?

print(listas[0][1])     # 2
print(listas[2][1])     # 8

# iterando com loops em uma lista aninhada
for lista in listas:
    for n in lista:
        print(n)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]
"""
# outros exemplos

# Gerando  um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# gerando jogadas para o jogo da velha

velha = [['x' if numero % 2 == 0  else 'o' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])























