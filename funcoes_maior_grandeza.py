"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa ?

- Quando uma linguagem de programação suporta HOF indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variaveis do tipo de funções
nos nossos programas.

OBS: Na seção de funções, nos ultlizamos isso.

Em python, as funções são cidadões de primeira classe, Firts Class Citizen


# Exemplo - Definindo as funções

def somar(a, b):
    return  a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções

print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))

# Nested Functions - Funções Aninhadas


#Em python podemos tambem ter funções dentro de funções, que são conhecidas por Nested Function ou
#Inner Functions (funções Internas).


# Exemplo

from random import choice

def Cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de voce '))
    return humor() + pessoa


# Testando

print(Cumprimento('Angelina'))

print(Cumprimento('Felicity'))

# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahahhahha ', 'kkkkkkkkkkkkkk ', 'hehehehehehhehe '))
    return rir

# testeando

rindo = faz_me_rir()
print(rindo())


"""

# Ineer Functions (funções internas / Nested Functions) podem acessar o escopo
# de funções mais externas.

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahah ', 'huehuehuehuehue ', 'kskskkskskskksks'))
        return f'{risada}  {pessoa}'
    return dando_risada


# testando

rindo = faz_me_rir_novamente('Fernanda ')

print(rindo())
print(rindo())
print(rindo())
















































