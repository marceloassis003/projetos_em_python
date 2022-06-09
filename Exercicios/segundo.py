

import primeiro

def funcao2():
    primeiro.funcao1()


if __name__ == '__main__':
    funcao2()
    print('segundo.py esta sendo executado diretamente')
else:
    print(f'O arquivo.py foi impotado. {__name__}')


