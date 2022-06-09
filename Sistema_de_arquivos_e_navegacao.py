"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do SO, precisamos
importar e fazer uso do modulo OS.

#   Fazer o import

import os

# getcwd() -> pega o current work directory - diretorio de trabalho corrente
#  Retorna o path (caminho) absoluto

print(os.getcwd())   # C:\Users\pc-prime\PycharmProjects\guppe

# Para mudar o diretorio, podemos ultlilizar o chdir()

os.chdir('..')

print(os.getcwd())  # C:\Users\pc-prime\PycharmProjects

os.chdir('..')

print(os.getcwd())  # C:\Users\pc-prime

os.chdir('..')

print(os.getcwd())  # C:\Users

os.chdir('..')

print(os.getcwd())  # C:\


#   Podemos checar se um diretorio é absoluto ou relativo

print(os.path.isabs('/home/geek/'))  # True


# OBS para usuários windows
# Tera que ter cuidado ao verificar diretorio

#print(os.path.isabs('C:\\Users\\pc-prime'))


# Podemos identificar o SO com o módulo os
print(os.name)



# Podemos ter mais detalhes do SO
print(os.uname())


print(os.getcwd())

res = os.path.join(os.getcwd(), 'geek')

os.chdir(res)

print(os.getcwd())

# VEja que o os.path.join() recebe dois parametros, sendo o primeiro o diretorio atual
# e o segundo o diretorio que será juntando ao atual.


# Podemos listar os diretorios com o listdir()

print(os.listdir())
"""

import os

# Podemos listar os arquivos e diretorios com mais detalhes com scandir()
scaner = os.scandir()

arquivos = list(scaner)

# print(arquivos)

print(arquivos[0].inode)  # ??
print(arquivos[0].is_dir)  # é um diretorio ? False
print(arquivos[0].is_file)  # é um arquivo? True
print(arquivos[0].is_symlink)  # é um link simbolico ? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até o arquivo
print(arquivos[0].stat)  # Estatisticas .....

# OBS: Quando ultlizamos a função scandir() nós precisamos fecha-la, assim quando abrimos um arquivo.

scaner.close()























