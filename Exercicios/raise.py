"""
Levantando os proprios erros com raise

raise -> Lança exceções

obs: raise nao é uma função. é uma palavra reservada, assim como def ou qualquer outra em python.

para simplificar, pense no raise como sendo ultil para que possamos criar nossas próprias exceções e mensagens
de erro.

A forma geral de ultilização é:

Raise   TipoDoErro('Mensagem de erro')

raise ValueError('valor incorreto')

# Exemplo real

def colore(texto,cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O {texto} sera impresso na cor {cor}')

colore(True , 'Blue')

# Exemplo Refatorado

def colore(texto,cor):
    cores = ('verde', 'amarela', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not  in cores:
        raise ValueError(f'A cor precisa ser uma entre:  {cores}')
    print(f'O {texto} sera impresso na cor {cor}')

colore('Geek University' , 'preto')

Obs: O raise assim como o return, finaliza a função, ou seja, nada após o raise é executado.
"""







































