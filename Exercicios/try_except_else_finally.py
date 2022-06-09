"""
Try / Except / Finaly

Dica de quando e onde tratar codigo:

TODA ENTRADA  DEVE SER TRATADA !

OBS: A função do usuario é destruir seu sistema.

# else -> É executado somente se não ocorrer o erro.
try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor invalido !')
else:
    print(f'Voce digitou {num}')

# Finally

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor invalido !')
else:
    print(f'Voce digitou {num}')
finally:
    print('Executando o finaly !')

# OBS: o bloco finaly é sempre executado. Independente se houve execução ou não.

# O Finally geralmente, é ultlizado para fechar ou desalocar recursos.


# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b

num1 = int(input('Informe o Primeiro numero: '))

try:
    num2 = int(input('Informe o Segundo numero: '))
except ValueError:
    print('O valor precisar ser numerico !')

try:
    print(dividir(num1, num2))
except NameError:
    print("Valor incorreto ")

# Exemplo mais complexo CORRETO
# Voce e responsavel pelas entradas das suas funções, Entao trate-as

def dividir(a, b):
   try:
        return int(a) / int(b)
   except ValueError:
       return  'Valor Incorreto'
   except ZeroDivisionError:
       return 'Não é possivel realizar uma divisão por 0'

num1 = input('Informe o Primeiro numero: ')
num2 = input('Informe o Segundo numero: ')

print(dividir(num1, num2))

# Exemplo mais complexo  - Generico
# Voce e responsavel pelas entradas das suas funções, Entao trate-as

def dividir(a, b):
   try:
        return int(a) / int(b)
   except:
       return 'Ocorreu um problema'

num1 = input('Informe o Primeiro numero: ')
num2 = input('Informe o Segundo numero: ')

print(dividir(num1, num2))


# Exemplo mais complexo  - Semi Generico
# Voce e responsavel pelas entradas das suas funções, Entao trate-as

def dividir(a, b):
   try:
        return int(a) / int(b)
   except (ValueError, ZeroDivisionError) as err:
       return 'Ocorreu um problema'

num1 = input('Informe o Primeiro numero: ')
num2 = input('Informe o Segundo numero: ')

print(dividir(num1, num2))

"""


























































