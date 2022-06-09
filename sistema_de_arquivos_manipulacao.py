"""
Sistema de arquivos - Manipulação


# Descobrindo se um arquivo ou diretorio existe

# Arquivo
print(os.path.exists('arquivo.txt'))    # False
print(os.path.exists('frutas.txt'))    # True


# Diretorio

#   Paths relativos
print(os.path.exists('exercicios'))    # True
print(os.path.exists('exercicios/geek'))    # True
print(os.path.exists('exercicios/geek/university/geek3.py'))    # True
print(os.path.exists('outro'))    # False

# paths absolutos
print(os.path.exists('/home/exercicios/geek/university'))    # False
print(os.path.exists('/home/exercicios/geek/Imagens'))    # True


# Criando arquivos

#   Forma 1
open('arquivo-teste.txt', 'w').close()

#   Forma 2
open('arquivo-teste2.txt', 'a').close()

#   Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass


os.mknod('arquivo-teste4.txt')

#   OBS:  Para MAC, pode haver um erro de PermissionError
#   OBS: Criando um arquivo via mknod() se o arquivo ja existir teremos o erro FileExistsError


# Criando diretorios

# Criandodiretorios - únicos (um a um)

#   path relativo
os.mkdir('templates')

#   path Absoluto
os.mkdir('C:\\Users\\pc-prime\\PycharmProjects\\guppe\\Exercicios\\geek\\templates')

#   OBS: A função mkdir() cria um diretorio se este nao exisitr. Caso exista , teremos FileExistsError


os.mkdir('/etc/templates')

#   OBS: Se não tivermos permissão para criar o diretorio teremos um PermissionError

# Criando multi-diretorios (arvore de diretorios)

# forma 1

os.mkdir('C:\\Users\\pc-prime\\PycharmProjects\\guppe\\templates')

os.mkdir('C:\\Users\\pc-prime\\PycharmProjects\\guppe\\templates\\geek')

os.mkdir('C:\\Users\\pc-prime\\PycharmProjects\\guppe\\templates\\geek\\university')

#   forma 2

os.makedirs('C:\\Users\\pc-prime\\PycharmProjects\\guppe\\templates\\geek\\university')

# obs: Se ja exisitr, teremos um FileExistsError


os.makedirs('C:\\Users\\pc-prime\\PycharmProjects\\guppe\\templates2\\novo2\\outro2', exist_ok=True)

# renomear arquivos e diretorios

#   Diretorios
os.rename('geek2/novo2', 'geek2')

# OBS: Se o diretorios nao existir teremos um FileNotFoundError

#   OBS: Se o diretorio que queremos renomear não estiver vazio teremos um OSError


# Arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')

# removendo arquivos

#  Atenção! Tenha cuidado com os comando de deleção, ao deletarmos um arquivo ou diretorio. Eles
# não vão para a lixeira. Eles somem.

os.remove('geek2/novo2/outro2/geek.txt')

# Se voce estiver no windows e o arquivo que voce for deletar estiver em uso, voce terá um erro.
# Caso o arquivo não exista, teremos o FileNotFoundError
# Se voce informar um diretorio ao inves de um arquivo, teremos um IsADirectoryError


# Removendo Diretorios - vazios

os.rmdir('templates')

# Se o diretorio tiver qualquer conteúdo teremos um OSError
# Se o diretorio não existir teremos FileNotFoundError


# Removendo uma arvore de diretorios
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# podemos remover uma árvore de diretorios vazios

os.removedirs('geek2/mais')

# Se algum dos diretorios tiver arquivos ou outros diretorios, o processo para.



# ATENÇÃO! : Ao remover arquivos e diretorios com python eles não vão para lixeiras ,
# eles são deletados permanentemente.



# importando a biblioteca send2trash    (Envia arquivos e diretorios para a lixeira)
from send2trash import send2trash

# arquivos

os.remove('cesta1.txt')      # Não vai para a lixeira. é deletado permanentemente

send2trash('cesta2.txt')    # Vai para lixeira. Pode ser restaurado.

# Se o arquivo não existir teremos OSError

# Diretorios

send2trash('teste')


# Criando um diretorio temporario

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o Diretorio temporario em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek univesity\n')
    input()

#   Estamos criando um diretorio temporario, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# os arquivos temporarios 'vivos' dentro dos blocos with.

# possivelmente, o codigo acima não ira funcionar com windows. por conta
# desse sistema trabalhar de forma diferente com arquvivos
# temporario.


# Criando um arquivo temporario

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# Em arquivos temporario só conseguimos escrever bits, por isso ultlizamos b''

# Sem o bloco with

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()


# Trabalhando com arquivos e diretorios temporarios

import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()

https://docs.python.org/3/Libray/os.html?highligth=os#module-os
"""



















