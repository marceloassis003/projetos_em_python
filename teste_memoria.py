"""
Teste de memoria cim Generators

Sequencia de Fibonacci

1, 1, 2, 3, 5, 8, 13....


#   Função usando listas 449mb

def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Teste 1 - listas 449 m

for n in fib_lista(100000):
    print(n)


# Função usando geradores

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# teste 2 geradores 4,8 MB

for n in fib_gen(100000):
    print(n)

"""










