"""
Escrevendo em arquivos

OBS: Ao abirir um arquivo para leitura, não podemos realizar a escreta nele,
apenas ler. Da mesma forma, se abrirmos um arquivo para escrita , não podemos le-lo somente escrever nele.

obs: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo ultlizamos a função write().
Esta função recebe uma string como parãmetro. Se não teremos um TypeError

- Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir sera criado,
caso ele ja exista, o anterior sera apagado e um novo sera criado. Dessa forma, todo
o conteudono arquivo anterior é perdido.


# Forma tradicional de escrita em arquivo (não pythonica)
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')

arquivo.close()


#   Exemplo de escrita - modo 'w' - Write (escrita) - pythonica

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('outros podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a ultlima linha.')


with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek \n' * 1000)

"""
with open('../frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break







































