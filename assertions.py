"""
Assertions (Afirmação/Checagens/Questionamentos)

Em python ultlizamos a palavra reservada 'assert' para realizar simples
afirmações ultlizamos nos testes.

Ultlizamos o 'assert' em uma expressão que queremos checar se é valida ou não.
Se a afirmaçao for verdadeira. retorna None e caso seja falsa levanta um erro
do tipo AssertionError.

# OBS: Nos podemos especificar, opcionalmente, um segundo argumento ou mesmo uma
mensagem de erro personalizada/

# OBS: A palavra 'assert' pode ser ultlizada em qualquer função ou codigo nosso...
não precisa ser exclusivamente nos testes.

# ALERTA: Cuidado ao ultlizar 'assert'

Se o programa python for executado com o parametro -O, nenum assertion
sera validade. ou seja, todas as suas validaçoes já eram.

"""

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os numeros precisam ser positivos'
    return a + b





ret = soma_numeros_positivos(2, 4)  #   6

#ret = soma_numeros_positivos(-2, 4)  #   AssertionError

#print(ret)

def comer_fast_food(comida):
    assert comida in [
        'piza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'

comida = input('Informe a comida: ')
print(comer_fast_food(comida))



def faca_algo_ruim(usuario):
    assert usuario.eh_admin, 'Somente administradores podem fazer coisas ruins'
    destroi_todo_o_sistema()
    return 'Adeus'

































