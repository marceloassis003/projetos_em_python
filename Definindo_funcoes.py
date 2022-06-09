"""
Definindo Funçoes

- são pequenos trechos de codigos que realizam tarefas especificas:
- pode ou não recebr entrar de dados e retornar uma saida de dados:
- uteis para executar procedimentos similares por repetidas vezes:
- para definir uma funçao ultilizamos a palavra reservada 'def'
"""

# exemplo de ultilizaçao de funções
cores = ['verde', 'amarelo', 'azul', 'branco']

# ultilizando a função integrada (Built-in)
print(cores)

curso = 'Programação em Python: Essencial'

print(curso)

cores.append('roxo')
print(cores)

# curso.append('Mais daods....')   # AttributeError

cores.clear()
print(cores)

# como definir funções
"""
a foram geral de definir uma função É:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
"""
# definindo a 1° função

def diz_oi():
    print('Oi !')

# ultilizando funções
diz_oi()

# exemplo 2

def cantar_parabens():
    print('Parabens pra voce')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print('Viva ao aniversariante !')

cantar_parabens()

for n in range(5):
    cantar_parabens()

# atribuindo a funçao a uma variavel
cantar = cantar_parabens

cantar()









