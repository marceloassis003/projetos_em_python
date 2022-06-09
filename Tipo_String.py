"""
TIPO STRING

"""

nome = 'Geek University'
print(nome)
print(type(nome))


nome = "Gina's Bar"
print(nome)
print(type(nome))


nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = """Angelina
Jolie"""
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split())     #transforma strings em lista

# [ 0,        1]
# ['Geek' , 'University']
nome = 'Geek University'

print(nome.split()[0])

print(nome.split()[1])

print(nome[::-1]) # inversao de string

print(nome.replace('e', 'i'))

print(type(nome))

texto = 'socorram me subino onibus em marrocos' # Palindrimo

print(texto)

print(texto[::-1])











