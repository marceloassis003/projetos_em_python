"""
O bloco with

Passos para se trabalhar com arquivos

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O block with é ultlizado para criar um contexto de trabalho onde os
recursos ultlizados são fechados após o bloco with.

arquivo = open('texto.txt)

"""
# o Bloco with - Forma pythonica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readline())
    print(arquivo.closed)


#print(arquivo.read())

print(arquivo.closed)

























