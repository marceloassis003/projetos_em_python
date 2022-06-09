"""
Map

- Com map, fazemos mapeamento de valores para função.
import math

def area(r):
    # Calcule a area de um circulo com raio 'r' .
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# forma 2
# Map é uma funaçao que recebe 2 parametros: O primeiro é uma funçao, o segundo é um iteravel

areas = map(area, raios)
print(areas)
print(type(areas))

print(list(areas))

# forma 3 - map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# obs :  apos ultilizar a função map() depois da primeira ultlizaçao do resultado, ele zera.

# para fixar - map

# temos dados iteraveis:

# dados: a1, a2, ..., an

# temos uma funçao:

# funçao: f(x)

# ultlizamos a funçao map(f, dados) onde map ira 'mapear' cada elemento dos dados e aplicar a função.

# O Map object: f(a1), f(a2), f(...), f(an)

"""
# mais um exemplo

cidades = [('berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

print(cidades)

# f = 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))















