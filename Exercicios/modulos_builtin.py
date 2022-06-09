"""
Trabalhando com Modulos Builtin (modulos integrado, que já vem instalados no pyrhon)
________________________
|python|Módulos builtin|
------------------------

https://docs.python.org/3/py-modindex.html

# Ulitlizando alias (apelidos) para modulos/funções.
import random as rdm

print(rdm.random())


# Podemos importar todas as funções de módulo ultlizando o *

from random import *

print(random())


# Importando todo o módulo

import random

print(random.random())


# ultlizando alias (apelidos) para modulos/funções

from random import randint as rdi

print(rdi(5, 89))


# ultlizando alias (apelidos) para modulos/funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

"""
# Costumamaos a ultlizar tuple para colocar multiplos imports de um mesmo mómudlo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['GEek', 'university', 'python']
shuffle(lista)
print(lista)

print(choice('University'))




















































