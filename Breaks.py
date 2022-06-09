"""
SAINDO DE LOOPS COM BREAK

obs -> para sair de loops de maneira projetda.
"""

#EXEMPLO 1

for num in range(1, 11):
    if num == 6:
        break
    else:
        print(num)
print('Sai do loop !')

# EXEMPLO 2

while True:
    comando = input("Digite 's' para sair")
    if comando == 's':
        break






