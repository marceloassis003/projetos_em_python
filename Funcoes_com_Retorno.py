"""
Funçoes com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

- quando uma funçao nao retorna nenhum valor, o retorno e None.
- funçoes python que retorna valores devem retornar esses valores com 'return'
- nao precisamo criar uma variavel para recber o retorno de uma funçao, podemos passar
a execuçao para outras funçoes.

informaçoes sobre return ->
- ela finaliza a funçao, ou seja, ela sai da execuçao da funçao:
- podemos ter, em fubçao, diferentes returns
- podemos, em uma função, retornar qualquer tipo de dado e ate mesmo multiplos valores
"""


# exemplo funçao
# refatorando a funçao para que ela retorna o valor

def quadrado_de_7():
    return 7 * 7


# criamos uma variavel para receber o retorno da funçao
ret = quadrado_de_7()
print(f'Retorno {ret}')

print(f'Retorno {quadrado_de_7()}')

# refatorando a primeira funçao

def diz_oi():
    return 'Oi !'

alguem = 'Pedro'

print(diz_oi())
print(alguem)

# exemplo 1 - ela finaliza a funçao, ou seja, ela sai da execuçao da funçao:

def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi !'
    print('Estou sendo executado após o retorno.....')

print(diz_oi())

# exemplo 2 - podemos ter, em fubçao, diferentes returns

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())
# exemplo 3 - podemos, em uma função, retornar qualquer tipo de dado e ate mesmo multiplos valores

def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

# exemplo 4 - Funçao jogando a moeda

from random import  random

def joga_moeda():
    valor = random()   # gera numeros randomicos entre 0 e 1
    if valor > 0.5:
        return 'Cara'
    else:
        return 'Coroa'

print(joga_moeda())

def jokey_pow():
    valores = random()
    print(valores)
    if valores > 0.23 and 0.33:
        return 'pedra'
    if valores <= 0.34 and 0.5:
        return 'Papel'
    else:
        return 'Tesoura'

print(jokey_pow())



# ERRO comuns na ultilziaçao do retorno

def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    else:
        return False

print(eh_impar())







