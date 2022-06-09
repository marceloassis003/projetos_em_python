"""
Decorators com Diferentes Assinaturas


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Ola eu Sou(a) {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, acompanhado de {acompanhamento}. por favor. '

# Teste

#print(saudacao('Angelina '))


print(ordenar('Picanha', 'Batata Frita '))

# Para resolver, ultlizamos um padrão de projeto Decorator Pattern

A assinatura de uma função e representada pelo seu retorno, nome e parâmetros de entrada.
# Relembrando

# Refatorando com a Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Óla, eu sou(a) {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, acompanhado de {acompanhamento}. por favor. '

print(saudacao('Felicity '))

print(ordenar('Picanha', 'Batata frita '))

@gritar
def lol():
    return f'lol'

print(lol())

# OBS: vale lemebrar que podemos ultlizar parâmetros nomeados

print(ordenar(acompanhamento='Batata Frita', principal='Picanha '))

"""

# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna
@verifica_primeiro_argumento('Pizza ')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(n1, n2):
    return n1 + n2

# Testando

print(soma_dez(10, 12)) # 22

print(soma_dez(1, 22))  # 22

print(comida_favorita('Pizza ', 'Churrasco '))

print(comida_favorita('Sanduiche ', 'Churrasco '))




