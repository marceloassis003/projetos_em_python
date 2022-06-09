"""
Modulo Random e o que são modulos ?

- Em python, modulos nada mais são do que outros arquivos python.

Modulo Random -> possui varias funçoes para geração de números pseudo-aleatorio.


# OBS: existem duas formas de se ultlizar um moduloou função deste

# Forma 1 - importando todo o modulo (Não recomendado).

import random

# random() -> Gera um numero real pseudo-aleatorio entre 0 e 1.

# OBS: Ao realizar o import de todo o modulo, todas as funções, atributos, classe e propriedades que estiverem
# dentro do modulo ficarão disponiveis (ficarão em memoria). Caso voce saiba quais funções voce precisa ultlizar
# deste modulo, então esta não seria a melhor forma ideal de ultlização. Nos veremos uma forma melhor na forma 2.

print(random.random())

# VEja  que para ultlizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função.
# separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é
# apenas uma função dentro do modulo random.


# Forma 2 - Importando uma função especifica do módulo (Forma recomendada).

from random import random

# no import acima estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())


# uniform() -> Gerar um numero real pseudo-aleatorio entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(5, 10))   # 10 não é incluido.


# randint() -> Gera valores inteiros pseudo-aleatorios entre os valore estabelecidos.

# Gerador de apostas para a mega-sena

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ') # começa em 1 e vai até 60

# Choice() -> Mostra um  valor aleatorio entre um iteravel.

jogadas = ['pedra', 'papel', 'tesoura']

from random import choice

print(choice(jogadas))


# Shuffle() -> Tem a função de enbaralhar dados.

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas.pop())
"""




from random import randint

for i in range(6):
    print(randint(1, 61), end=', ') # começa em 1 e vai até 60























