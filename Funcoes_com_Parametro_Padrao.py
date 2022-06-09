"""
Funçoes com parametro Padão - default paramters)

- Funçoes onde a passagem de parametro seja opcional:
# exemplo onde a passagem de parametro seja opcional:
print('Geek University')

print()
"""

# exemplo de funçao onde a passagem de parametro e obrigatoria

def quadradro(numero):
    return numero ** 2


print(quadradro(3))
print(quadradro()) #TypeError

def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))   # por padrao eleva ao quadrado
print(exponencial(3, 5))    # eleva a potencia informada pelo usuario

# obs
# se o usuario passar somente 1 argumento, este sera atribuido ao parametro numero,
# e sera calculado o quadrado deste numero

print(exponencial())

# em funçoes python os parametros com valores default DEVEM sempre estar ao final da declaraçao

# erro !

def teste(potencia, num=2):
    return num ** potencia

print(teste(6))

# outros exemplos
def soma(num1=3, num2=7):
    return num1 + num2

print(soma(4, 3))
print(soma(4))      #typeerror
print(soma())       #typeerror

# exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor geek !'
    elif nome == 'Geek':
        return 'Eu pensei que voce era o instrutor '
    return f'Ola {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

# exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - evitar problemas

# variaveis globais
# variaveis locais

instrutor = 'Geek'   # variavel global

def doz_oi():
    instrutor = 'Python'        #variavel local
    return f'Oi {instrutor}'

print(doz_oi())

# exemplo
def diz_oi():
    prof = 'Geek'   #variavel local
    return f'Ola {prof}'

print(diz_oi())

print(prof)         #nameError 

# principios de variaveis globais - ( evite variaveis globais)

total = 0

def encrementa():
    total = total + 1   # UnboundLocalError ( variavel nao foi inicializada)
    return total

print(encrementa())

# principios de variaveis globais - ( evite variaveis globais)

# resoluçao 

total = 0

def encrementa():
    global total        # avisando que a variavel é global
    total = total + 1
    return total

print(encrementa())
print(encrementa())
print(encrementa())

# funçoes declaradas dentro de funçoes

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

print(dentro())   # funçao interna












