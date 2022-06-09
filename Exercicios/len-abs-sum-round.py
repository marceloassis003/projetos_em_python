"""
Len, Abs, Sum, Round

#  len

len() - > retorna o tamanho (ou seja, o numero de itens) de um iteravael.

# so pra revisar

print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))

# Por debaixo dos panos, quando ultilizamos a funçao len() o python faz o seguinte:

# Dunder len
print('Geek University'.__len__())

# Abs

abs() -> retorna o valor absoluto de um numero intyeiro ou real. De forma basica, seria o seu valor real sem o sinal.

# exemplos abs

print(abs(-5))
print(abs(5))
print(abs(3.13))
print(abs(-3.13))

# Sum

sum() -> recebe como parametro um iteravel, podendo receber um valor inicial, e retorna a soma total dos elementos,
incluindo o valor inicial.

#obs: o valor inicial default = 0

# Exemplos sum

print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))

print(sum([3.145, 5.678]))

print(sum((1, 2, 3, 4,  5)))

print(sum({1, 2, 3, 4,  5}))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

# Round

round() -> retorna um numero arrendondado para para n digito de precisão apos a casa decimal. Se a precisão não for
informada retorna o inteiro mais proximo da entrada.
"""
# exemplos Round

print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(1.2121212121, 2))

print(round(1.21999999, 2))



































