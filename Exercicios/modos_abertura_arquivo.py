"""
Modos de abertura de Arquivos

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve casao o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o conteudo ao final do arquivo .
+ -> Abre para  modo de arualização: Leitura e escrita.

# obs: Abrindo no modo 'a' -> append, se o arquivo não existir será  criado. Caso exista, o novo conteúdo
seá adicionado SEMPRE ao final. Com o modo 'a', nao controlamos o cursor.(temos o controle do cursos)

http://docs.python.org/3/library/functions.html#open

# Exemplo x
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo. \n')
except FileExistsError:
    print('Arquivo ja existe')

# Exemplo A


with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input("informe uma fruta ou sair: ")
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break


# Exemplo r+
with open('outro.txt', 'r+') as arquivo:
    #arquivo.seek(0)
    arquivo.write('Adicionada\n')
    arquivo.seek(11)
    arquivo.write('Nova Linha.\n')
    arquivo.seek(12)
    arquivo.write('Mais uma linha.\n')

"""







