"""
Escrevendo em arquivos CSV

reader() (leitor), Writer() (escritor)

writerow() -> Escreve uma linha


# writer() -> Gera um objeto para que posamos escrer em um arquivo CSV. Ultlizamos o
# metodo writerow() para escrever cada linha. Este método recebe uma lista.

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])
"""

# DictWriter

# OBS: As chaves do dicionario devem ser as mesmas ultlizadas como cabeçalho.

from csv import DictWriter


with open('filmes.csv', 'w') as arquivo:
    cabecalho = ['Titulo', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({"Titulo": filme, "Gênero": genero, "Duração": duracao})








































