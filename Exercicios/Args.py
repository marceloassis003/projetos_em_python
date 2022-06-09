"""   
entendendo o * args

- o "args" é um paramentro como outro qualquer , pode ser nomeado de sua preferencia des de que começe com "*"

#exemplo
def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))

print(soma_todos_numeros(4, 6, 9, 5))

# entendo o args
def soma_todos_numeros(noem, email, *args):
   return sum(args)

print(soma_todos_numeros('jose', 'travolta'))
print(soma_todos_numeros('jose', 'travolta', 1))
print(soma_todos_numeros('jose', 'travolta', 2, 3))
print(soma_todos_numeros('jose', 'travolta', 2, 3, 4))
print(soma_todos_numeros('jose', 'travolta', 3, 4, 5, 6))

print(soma_todos_numeros('jose', 'travolta', 23.4, 12.5))

# outro exemplo de ultilizaçao do *args

def verifica_info(*args):
    if 'geek' in args and 'university' in args:
        return 'Bem-vindo geek!'
    return 'Eu nao tenho certeza de quem voce é.....'

print(verifica_info())
print(verifica_info(1, True, 'university', 'geek'))
print(verifica_info(1, 'university', 3.145))


"""
def soma_todos_numeros(*args):
   return sum(args)

#print(soma_todos_numeros())
#print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]



# desempacotador

print(soma_todos_numeros(*numeros))

# o '*' serve para informar ao python que estamos passando
#como  argumento uma coleçao de dados, desta forma ele ira saber que antes
# precisa desempacotar esses dados











