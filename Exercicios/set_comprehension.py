"""
Set Comprehension

lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}

"""
# exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# outro exemplo

numeros = {x ** 2 for x in range(10)}

print(numeros)

# desafio: faça uma alteraçao na estrututa acima para gerar um dicionario ao inves de set

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Para Finalizar

letras = {letra for letra in 'Geek University'}

print(letras)





















