"""
**kwargs

Este é so mais um parametro, mas diferente do *args que coloca os valores extras
em uma trupla, o **kwargs exige que ultilizemos parametros nomeados, e transforma esses
parametros extras em um dicionario.

# nas nossas funçoes, podemos ter (nesta ordem):

- parametros obrigatorios;
- *args
- parametros default (nao obrigatorios);
- **kwargs


# Exemplo
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favoritade {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# obs: nem os parametros *args e **kwargs nao sao obrigatorios.

cores_favoritas()

cores_favoritas(geek='navy')

# exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs ['geek'] == 'phyton':
        return 'voce recebeu um cumprimento pythonico geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem voce é........'

print(cumprimento_especial())
print(cumprimento_especial(geek='python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)


minha_funcao(8, 'julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='nao', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entenda por que é importante manter a ordem dos parametros na declaraçao

#funçao com a ordem correta de parametros

def mostra_info(a,b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


a = 1
b = 2
args = (3, )
instrutor= 'Geek'
kwargs = {'sobrenome': 'university', 'cargo': 'Instrutor'}


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jone'}

print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c )

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}


soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# obs: os nomes das chaves em um dicionario devem ser os mesmos dos parametros da funçao

# dicionario = dict(d=1, e=2, f=3)   #typeError
#soma_multiplos_numeros(**dicionario)

dicionario = dict(a=1, b=2, c=3, nome='Geek')


soma_multiplos_numeros(**dicionario, lang='python')

"""














