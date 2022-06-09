"""
Seek e Cursosrs

seek() -> É ultlizada para movimentar o cursor pelo arquivo.



arquivo = open('texto.txt')

print(arquivo.read())

# seek() -> A função seek é ultlizada para movimentação do cursor pelo arquivo. Ela recbe
# um parametro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivo com afunção seek() -> Procurar

arquivo.seek(0)

print(arquivo.read())

arquivo.seek(22)

print(arquivo.read())


# readLine() -> Função que le o arquivo linha a linha (readline -> lê linha )

ret = arquivo.readline()

print(type(ret))

print(ret)

print(ret.split(' '))


# readlines()

linhas = arquivo.readlines()

print(len(linhas))

# obs: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trablahos com o arquivo devemos fechar essa conexão. Para isso ultlzamos a função close().

Passos para se trablahar com um arquivo:

1 - Abir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo ;


# 1 - Abir o arquivo;
arquivo = open('texto.txt')

#   2 - Trabalhar o arquivo;
print(arquivo.read())

print(arquivo.closed)   #False / verifica se o arquivo esta aberto ou fechado

#   3 - Fechar o arquivo ;
arquivo.close()

print(arquivo.closed)   #True / verifica se o arquivo esta aberto ou fechado

print(arquivo.read())

# OBS: se tentarmos manipular o arquivo apos seu fechamento, teremos um ValueError


"""

arquivo = open('texto.txt')

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(50))




























































