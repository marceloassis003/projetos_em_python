"""
Modulo Collections - Counter (contador)

Collections -> hig-perfomace container Datetypes

Counter -> recebe um interavel como parametro e cria um objeto do tipo collections counter que é parecido
com um dicionarios, contendo chave o elemento da lista passada como parametro e como valor a quantidade de
ocorrencias desse elemento

"""


# exemplo 1 - ultilizando o Counter

# realizando o import
from collections import Counter

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 7, 23, 44, 87, 13, 66, 45, 34]

# ultilizando o counter
res = Counter(lista)

print(type(res))

print(res)
# para cada elemento da lista, o counter criou uma chave e colocou como valor a quantidade de ocorrencias.

# exemplo 2 - contando strings 
from collections import Counter

print(Counter('Geek University'))

from collections import Counter

# exemplo 3 -

texto = """  Inteligência artificial (por vezes mencionada pela sigla em português IA ou pela sigla em inglês AI - artificial 
intelligence) é a inteligência similar à humana exibida por mecanismos ou software, além de também ser um campo de estudo acadêmico.
 Os principais pesquisadores e livros didáticos definem o campo como "o estudo e projeto de agentes inteligentes", 
 onde um agente inteligente é um sistema que percebe seu ambiente e toma atitudes que maximizam suas chances de sucesso. 
 Andreas Kaplan e Michael Haenlein definem a inteligência artificial como “uma capacidade do sistema para interpretar corretamente 
 dados externos, aprender a partir desses dados e utilizar essas aprendizagens para atingir objetivos e tarefas específicos através
  de adaptação flexível”.[1] John McCarthy, quem cunhou o termo em 1956 ("numa conferência de especialistas celebrada em Darmouth 
  Colege" Gubern, Román: O Eros Eletrónico), a define como "a ciência e engenharia de produzir máquinas inteligentes". É uma área de 
  pesquisa da computação dedicada a buscar métodos ou dispositivos computacionais que possuam ou multipliquem a capacidade racional 
  do ser humano de resolver problemas, pensar ou, de forma ampla, ser inteligente. Também pode ser definida como o ramo da ciência da
   computação que se ocupa do comportamento inteligente[2] ou ainda, o estudo de como fazer os computadores realizarem coisas que, 
   atualmente, os humanos fazem melhor.[3]
"""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(10))









