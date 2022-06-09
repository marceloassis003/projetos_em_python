"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamada datetime

2020-08-05 20:47:38.845602

2020-08-05 20:52:38.845602


#   print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

# Retorna a data e hora corrente

print(datetime.datetime.now())  # 2020-08-05 20:47:38.845602  BR 05/08/2020

# datetime.datetime(yer, month, day, hour, minute, second, microsecond)

print(repr(datetime.datetime.now()))

# Replace () para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horario para 22 horas, 0 minutos, 0 second, 0 microsecond
inicio = inicio.replace(year=2023, hour=22, minute=0, second=0, microsecond=0)

print(inicio)

# Recebendo dados do usario e convertendo para data


print(type(evento))
print(type('31/12/2018'))

print(evento)

print(evento)

nascimento = input('Informe sua data de nascimento (dd/mm/yyy): ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))


"""
import datetime

evento = datetime.datetime.now()

# Acesso individual dos elementos da data e hora

print(evento.year)  # Ano
print(evento.month) # mes
print(evento.day)   # dia
print(evento.hour)  # hora
print(evento.minute)    # minutos
print(evento.second)    # segundos
print(evento.microsecond)   # microsegundos

print(dir(evento))




















