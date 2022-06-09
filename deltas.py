"""
Trabalhando com deltas de data e hora

data_inicial  = dd/mm/yyy 12:55:34.99989
data_final = dd/mm/yyy 13:34:23.99542

delta = data_final  - data_inicial


import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2021, 3, 3, 0)

# Calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento)

print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas...')







"""

import datetime

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)



































