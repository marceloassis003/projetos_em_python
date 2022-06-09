"""
Reduce

obs: a partir do python3+ a funçao reduce() não é mais uma função integrada (built-in)
- Agora temos que importar e ultilizar esta função a partir do modulo 'functools'

Guido Van Rossum: Ultilize a função reduce() se voce realmente precisa dela. Em todo caso,
99% das vezes um loop FOR é mais legivel.

Para entender o reduce()

# imagine que voce tenha uma coleçao de dados:

dados = [a1, a2, a3, ..., an]

# E voce  tem uma função que recebe dois parametros:

def funcao(x, y):
    return x * y

Assim como map() e filter() a função reduce() recebe dois parametros: a função e o iteravel

reduce(funcao, dados)

A funçao reduce(), funciona da seguinte forma:
    Passo 1: res1 = f # aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # aplica a função passando o resultado do passo1 mais o 3° elemento e guarda o res.

    Isso é repetido ate o final.
    Passo3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resm, an)

Ou seja em cada psso ela aplica a função passando como 1° argumento o resultado da  aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""

# como funciona na prática

# vamos ultlizar a função reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para ultlizar o reduce() nós precisamos de uma função que recebe dois parametros
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# ultilizando um loop normal

res = 1
for n in dados:
    res = res * n

print(res)



















