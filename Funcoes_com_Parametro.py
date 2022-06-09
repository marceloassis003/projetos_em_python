"""
Funçoes com Parametro (de entrada)

-  Funçoes que recebem dados para serem processados dentro da mesma:



# refatorando uma funcao

def quadradro(numero):
    return numero ** 2


print(quadradro(7))
print(quadradro(2))
print(quadradro(5))

ret = quadradro(6)
print(ret)

# Refatorando a funçao

def cantar_parabens(aniversariante):
    print('Parabens pra voce')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print(f'Viva ao {aniversariante} !')

cantar_parabens('Marcos')

# funcoes podem ter n parametros de entrada

# exeplo

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek'))
print(outra(5, 4, 'Python'))

#print(soma(2, 3, 4)) # TypeError
#print(soma(4))  # TypeError

# nomeando parametros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo É: {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))

# diferença entre Parãmetros e Argumentos

# parametros sao variaveis declaradas na defiçao de uma funçao:
# argumentos sao dados passados durante a execuçao de uma funçao:

# a ordem dos parametros importa !

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (keyword arguments)

# caso ultilizamos nomes dos parametros nos argumentos para informa-los, podemos
# ultilizar qualquer ordem

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=None, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))




"""


# erro comum na ultilizaçao do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
             total = total + num
        return total

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))







