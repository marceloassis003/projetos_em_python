"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa
ter permissão:
    - Permissão de leitura para ler o arquivo
    - Permissão de escrita para escrever o arquivo

StringIO -> Ultlizado para ler e criar arquivos na memoria.

"""
# Primeiro fazemos o import

from io import StringIO

mensagem = 'Esta é apenas uma string normal'

# podemos criar um arquivo em memória ja com uma string inserida  ou mesmo  vazio  para inserirmos texto depois

arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos ultlizar tudo que ja sabemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write(' Outro Tetxo')

# podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())





















