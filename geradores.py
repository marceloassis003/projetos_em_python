"""
Geradores

 - Geradores (generators) são Iterators (Iteradores):

O contrario não é verdadeiro. Ou seja, nem todo iterator é um generator.

outras informações:

- Generators podem ser criados com funções geradoras;
- Funçoes geradoras ultlizam a palavra yiels;
- Generators podem ser criados com Expressões Geradoras;

Diferença entre funçoes e Generator Functions (funções geradoras)

--------------------------------------------------------------------------------
| Funções                                | Generator Functions                  |
--------------------------------------------------------------------------------
| Ultlizam return                        | ultlizam yield                       |
--------------------------------------------------------------------------------
| retorna uma vez                       | Podem ultlizar yield multiplas vezes  |
--------------------------------------------------------------------------------
| quando executado, retorna um valor    | quanto executada, retorna um generator |
---------------------------------------------------------------------------------


gen = conta_ate(5)

for num in gen:
    print(num)

# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


print(next(gen)) #  1

print('-------------')

for num in gen:
    print(num)


"""
# Exemplo Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

#   OBS: Uma Generator Function não é um generator. Ela gera um generator.


gen = list(conta_ate(10))

print(gen)














