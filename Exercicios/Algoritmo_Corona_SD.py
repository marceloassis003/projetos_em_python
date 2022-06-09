
"""
Exercicio corona virus - materia sistemas distribuidos

Marcelo Assis
n1812e-6
SI7P13
"""
import math
import random

#a = (math.ceil(10 * random.random()))
#numeros = range(1, 10)
#print(random.choice([25, 18, 32, 41, 17]))

# matriz 4 x 4
matriz = [[25, 18, 32, 41], [16, 26, 35, 29], [8, 47, 4, 94], [41, 88, 35, 1]]

print(random.choice(matriz))


for x in range(0, 4):
    for z in range(0, 4):
     if matriz == [16, 26, 35, 29]:
         print('Corona virus')
     elif matriz == 25:
         print('Corona virus')
     elif matriz == 32:
         print('Corona virus')
     elif matriz == 41:
         print('Corona virus')
     elif matriz == 17:
         print('Corona virus')
     else:
         print('Voce nao esta infectado')



