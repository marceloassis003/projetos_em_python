"""
Pacotes

Mpodulo -> é apenas um arquivo python que pode ter diversar funções para ultilizarmos

PAccote -> É um diretorio contendo uma coleção de módulos:

OBS: Nas versões 2.x  do python, um pacote python deveria conter dentro dele um
arquivo chamado __init__.py

Nas versões do python 3.x, não é mais obrigatorio a ultlizção deste arquivo, mas
normalmente ainda é ultlizado para manter compatibilidade.


from geek import geek1, geek2

from geek.university import geek3, geek4

print(geek1.pi)

print(geek1.funcao1(4, 6))

print(geek2.curso)

print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())

"""

from geek.geek1 import funcao1
from geek.university.geek4 import funcao4

print(funcao1(6, 9))

print(funcao4)









































