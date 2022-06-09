"""
Módulos customizados

Como módulo python nada mais são do que arquivos python, então TODOS os arquivos que criamos
neste curso são módulos python prontos para serem ultlizados.

# importando uma função especifica do nosso módulo
from Funcoes_com_Parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# importando todo o módulo (Temos acesso a TODOS os elementos do módulo)
import Funcoes_com_Parametro as fcp

# Estamos acessando e imprimindo uma variavel contida no módulo
print(fcp.lista)

print(fcp.tupla)

print(fcp.soma_impares(fcp.lista))
"""
from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))







































