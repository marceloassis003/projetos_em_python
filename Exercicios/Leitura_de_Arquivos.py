"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em python, ultilizamos a fiunção integrada open(),
que literalmente significa 'Abrir'

open() -> Na forma mais simples de ultlização nos passamos apenas um parametro de entrada
que neste caso é o caminho para o arquivo a ser lido. Essa função retorna um _io.TextIOWrapper
e é com ele que trabalhamos então.

# OBS: Por padrão, a função open() abre o arquivo para leitura, Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r -> Modo de leitura. r-> read() -> ler
"""

# exemplo

arquivo = open('texto.txt')

#print(arquivo)

#print(type)

# Para ler o conteudo de um arquivo, após sua abertura, devemos ultlizar a função read()

ret = arquivo.read()

print(type(ret))

print(ret)

#   OBS: o Python ultilia um recurso para trabalhar com arquivos chamado cursos. Esse cursor,
#   funciona como o cursor quando estamos escrevendo.

# print(arquivo.read())

# A função read() lê todo o conteudo do arquivo.

