"""
Módulos Externos

ultlizamos o gerenciado de pacote python chamado PIP - > Python Installer Package

VOce pode conhecer todos os pacotes oficiais em: https://pypi.org

Colorama -> É ultlizado para permitir impressão de textos coloridos no terminal.

Instalando um módulo:

pip install nome-do-módulo

- Instalando o pacote colorama

pip install colorama

- ultlizando o pacote instalado


from colorama import init, Fore

init()

print(Fore.MAGENTA + 'GEeek University')
print(Fore.RED + 'GEeek University')
"""
import pydf

pdf = pydf.generate_pdf('<h1>Geek University </h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)



















































