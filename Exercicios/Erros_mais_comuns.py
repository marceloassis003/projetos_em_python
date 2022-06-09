"""
Erros mais comuns em python

ATENÇÃO ! é importante prestar atenção e aprender a ler as saida de erros geradas pela execuçao
do nosso codigo.

Os erros mais comuns:

1 - SintaxError -> Ocorre quando o python encontra um erro de sentaxe, ou seja, voce escreveu algo que
o python nao reconhece como parte da linguagem.

Exemplos SyntaxError

a)
def funcao:
    print('geek university')

b)
    def = 1

c)

return

2 - NameError -> Ocorre quando uma variavel ou funçao não foi definida

a)
print(geek)
#  Exemplos NameError

a = 18

if a < 10:
    msg =  'é maior que 10'

print(msg)

3 - TypeError -> Ocorre quando uma funçao/operaçao/açao é aplicada a um tipo errado.

a)
print(len(5))

b)
print('geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado ultilizando
um indice invalido.

Exemplos IndexError

a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[0][10])

c)
tupla = ('Geek')
print(lista[0][10])

5 -> Ocorre quando uma funçao/operação built-in (integrado) recebe um argumento como tipo correto
mas valor inapropriado.

Exemplos ValueError

a)
print(int('Geek'))

6 -> KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave que não existe.

Exemplos KeyError

a)
dict = {'py': 'university'}
print(dict['geek'])

7 -> AttributeError : Ocorre quando uma variavel não tem um atributo/função.

Exemplos AttributeError

a)
tupla = (11, 2, 31, 4)
print(tupla.sort())

8 -> IdentationError : Ocorre quando não respeitamos a indentação do phyton ( 4 espaços)

Exemplos IdentationError

a)
def nova():
print('geek')

b)
for i in range(10):
i + 1

OBS: Exceptions e Erros são sinonimos na programação.

OBS: Importante ler e prestar atenção na saida de erro.
"""






























