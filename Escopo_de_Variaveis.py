"""
ESCOPO DE VARIAVEIS
"""
numero = 42  # Exemplo variavel Global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 42

if numero > 10:
    novo = numero + 10 # variavel 'novo' trata-se de uma variavel local
    print(novo)

