"""
TUPLAS (tuple)

obs: se parecem com listas
regras ->
1 - tuplas sao representadas por ()
2 - tuplas sao imutaveis (ao se criar nao muda, operacoes geram novas tuplas)
3 - conslusoes: tupulas sao definidas pela ',' e nao pelos '()'
(4) -> nao e tupla
(4,) -> é tupla
"""

# introducao
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# exemplo 1 - tuplas com 1 elemento
tupla3 = (4)
print(tupla3)

print(type(tupla3))

tupla4 = (4,)
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))
# exemplo 2 - tupla gerada dinamicamente com range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))
# exemplo 3 - desempacotamento de tupla
tupla = ('Geek University', 'programacao em python essencial')

escola, curso = tupla

print(escola)
print(curso)
# exemplo 4 - metodos para adicao e remocao nas tuplas nao existem (regra 2)

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
# exemplo 5 - concatenacao de tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)

tupla1 = tupla1 + tupla2
print(tupla1)
# exemplo 5 - verificar determinado elemento contidos na tupla
tupla = (1, 2, 3)

print(3 in tupla)
# exemplo 6 - iterando sobre uma tupla
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
# exemplo 7 - contando elemntos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tuple('Geek university')
print(escola)

print(escola.count('e'))
# exemplo 8 - dicas na ultilizacao de tuplas
# exemplo 1 - tuplas sempre que nao precisarmos alterar dados da colecao
meses = ('janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')


# exemplo 2 - acesso de elementos
print(meses[5])

# iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1
# exemplo 9 - verificando em qual indice o lemento esta na tupla
meses = ('janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

print(meses.index('junho'))
# exemplo 10 - slicing
meses = ('janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

print(meses[5:9])

# por que ultilizar tuplas ?

# motivo 1 - tuplas sao mais rapidas
# motivo 2 - deixam seu codigo mais seguro (regra 2)

# exemplo 11 - copiando tuplas
tupla = (1, 2, 3)
print(tupla)

nova = tupla
                    # nao tem problema de shallow copy
print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)





















