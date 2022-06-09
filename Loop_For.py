"""
ESTRUTURAS DE REPETIÇÂO
LOOP FOR
"""
# Exemplo de for 1 (iterando sobre uma string)
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)

for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)

for numero in range(1, 10):
    print(numero)
    
# Exemplo 4 Enumerate 
(0, 'G'), (1, 'e'), (2, 'e'), (3, 'k').........
for i, v in enumerate(nome):
    print(nome[i])

for _, letra in enumerate(nome):  #descartando um valor com (_)
    print(letra)
    
for valor in enumerate(nome):
    print(valor)
#exemplo 5 
qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é  {soma}')

# Exemplo 6 
nome = 'Geek University'

for letra in nome:
    print(letra, end='')
    
# Exemplo 7 (emoji) 
# original -> U+1F60F
# modificado -> U0001F60F

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60F' * num)









