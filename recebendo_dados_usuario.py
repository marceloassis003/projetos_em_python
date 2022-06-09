""""
Recebendo dados do usuario
"""
# Entrada de dados

nome = input('qual seu nome ?')


#print('Seja bem-vido(a)  %s' % nome)

#exemplo atual de print 3.7
print(f'Seja bem-vido(a) {nome}')

idade = int(input('Qual sua Idade?'))


# processamento

# Saida de dados
#print('A %s tem %s anos' % (nome,  idade))

#exemplo atual de print 3.7
print(f'A {nome} tem {idade} anos')

print(f'A {nome} nasceu em {2020 - idade}')
