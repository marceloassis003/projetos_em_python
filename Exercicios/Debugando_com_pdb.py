"""
Debugando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto

# OBS: A ultilização do print() para debugar codigo é uma pratica ruim.
def dividir(a, b):
   print(f'a={a}, b={b}')
   try:
        return int(a) / int(b)
   except:
       return 'Ocorreu um problema'

print(dividir(4, 7))


# existem formas mais profissionais de se fazer esse 'debug', ultlizando o debugger
# em python, podemos fazer isso em diferentes IDEs, como Pycharm ou ultlizando
# o PDB - python debugger

# exemplo como o pycharm

def dividir(a, b):
   try:
        return int(a) / int(b)
   except:
       return 'Ocorreu um problema'

print(dividir(4, 0))


# Exemplo com PDB, python Debugger - exemplo 1

# Para  ultlizar o python Debugger, precisamos* importar a biblioteca pdb e então ultlizar a função set_trance()

# Comando basicos do pdb
# l (listar onde estamos no código)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programção em python: Essencial '
final = nome_completo + ' faz o curso  ' + curso
print(final)

# Exemplo com PDB, python Debugger - exemplo 2

# Para  ultlizar o python Debugger, precisamos* importar a biblioteca pdb e então ultlizar a função set_trance()

# Comando basicos do pdb
# l (listar onde estamos no código)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)


nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programção em python: Essencial '
final = nome_completo + ' faz o curso  ' + curso
print(final)

# por que ultlizar este formato ?
# O debug é ultlizado durante o desenvolvimento, custumamos realizar todos os imports de bibliotecas
# no inicio do arquivo. Por isso, ao inves de colocarmos o immport do pdb no inicio do arquivo.
# nós colocamos somente onde vamos debuggar, e ao finalizar ja fazemos a remoção.


# Exemplo com PDB, python Debugger - exemplo 3

# Para  ultlizar o python Debugger, precisamos* importar a biblioteca pdb e então ultlizar a função set_trance()

# * A partir do python 3.7, não é mais necessario importar a biblioteca pdb, pois o comando de debug foi
# incorporado como função built-in (integrada) chamada breakpoint()

# Comando basicos do pdb
# l (listar onde estamos no código)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execução - finaliza o debugging)


nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programção em python: Essencial '
final = nome_completo + ' faz o curso  ' + curso
print(final)


# OBS: Cuidado com conflitos entre nomes de variaveis, e os comando do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))

# Como os nomes das variaveis são os mesmo dos comandos pdb, devemos ultlizar os comando p para imprimir
# as variaveis, ou seja: p nome_da_variavel

# Não coloque nomes representativos em variaveis. Sempre optar por nomes significativos.

# exemplo variaveis significativas ->

def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4
"""
























