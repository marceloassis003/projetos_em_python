"""
O block try/except

ultilizamos o bloco try/except para tratar erros que podem ocorrer no nosso codigo. Previnindo assim que
o programa pare de funcionar e o ususario receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problematica
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - tratando um erro genérico

try:
    geek()
except:
    print('Deu pau !')

# tente executar a função geek(), caso voce encontre erros, impirma a mensagem de erro.

# Exemplo 2 - tratando um erro genérico

try:
    len(5)
except:
    print('Deu pau !')

# tente executar a função geek(), caso voce encontre erros, impirma a mensagem de erro.

obs: tratar erro de forma generica nao é a melhor forma de tratamento de erros. O ideal é SEMPRE
tratar na forma especifica.

# Exemplo 3 - tratando um erro especifico

try:
    geek()
except NameError:
    print('Voce esta ultilizando uma funçao inexistente')

# Exemplo 4 - tratando um erro especifico

try:
    len(5)
except TypeError:
    print('Voce esta ultilizando uma funçao inexistente')


# Exemplo 5 - tratando um erro especifico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação geou o seguinte erro: {err}')

# exemplo 6 - podemos efetuar diversos tratamentos de erros de uma vez.

try:
    #len(5)
    geek()
    #print('Geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra} ')
except TypeError as errb:
    print(f'Deu TypeError: {errb} ')
except:
    print('Deu um erro diferente')
"""
def paga_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "geek"}


print(paga_valor(dict, 8))




























