"""
Modulo Colletions - Deque

Deque -> lista de alta performace.

"""
# realizando o import
from collections import deque

deq = deque('geek')

print(deq)

# adicionadno elemtnos no deque
deq.append('y') # adiciona no final

print(deq)

deq.appendleft('k')  # adiciona no começo da lista

print(deq)

# removendo elemntos
print(deq.pop())    # Remove e retorna o ultimo elemento

print(deq)

print(deq.popleft())    # Remove e retorna o 1° elemento

print(deq)




