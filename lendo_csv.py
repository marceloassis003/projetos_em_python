"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separadps por Virgula

# Sepador por virgula

1, 2, 3, 4, 5, 6

"geek", "University", "python", "cinencia", "dados"

#   Separador por ponto e virgula

1; 2; 3; 4; 5; 6

"geek"; "University"; "python"; "cinencia"; "dados"

# Separador por espaço

1 2 3 4 5 6

"geek" "University" "python" "cinencia" "dados"

http://dados.gov.br/dataset


# Possivel de se trabalhar, mas não é o ideal  (trabalhoso)
with open('lutadores.csv',  encoding='utf-8') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

A linguagem pyton possui duas formas diferentes para ler dados em arquivos csv:

    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteramos sobre as linhas do arquivo CSV como OrderDirects;

    # Reader

from csv import reader

with open('lutadores.csv',  encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)    # Pular o cabeçalho
    for Linha in leitor_csv:
        # cada linha é uma lista
        print(f'{Linha[0]} nasceu no(a) {Linha[1]} e mede {Linha[2]} centimetros ')


# DictReader

from csv import DictReader

with open('lutadores.csv',  encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for Linha in leitor_csv:
        # cada linha é uma lista
        print(f"{Linha['Nome']} nasceu no(a) {Linha['País']} e mede {Linha['Altura (em cm)']} centimetros ")
"""

# DictReader com outro separador

from csv import DictReader

with open('lutadores.csv',  encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for Linha in leitor_csv:
        # cada linha é uma lista
        print(f"{Linha['Nome']} nasceu no(a) {Linha['País']} e mede {Linha['Altura (em cm)']} centimetros ")








































































