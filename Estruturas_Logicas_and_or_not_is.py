"""
ESTRUTURAS LOGICAS -> AND (E), OR (OU), NOT (NÃO), IS (É)

Regras

- Para o 'and', ambos valores precisam ser True
- Para o 'or', um ou outro valor precisa ser True
- para o 'not', o valor de booleano e invertido , Ex:  True -> False / False -> True
- para o 'is' , o valor e comparado com o segundo
"""
ativo = True
logado = False

if not ativo:
    print('Voce precisa ativar sua conta check seu e-mail')
else:
    print('Welcome User  !')

print(ativo is True)

""" 
if ativo or logado:
    print('Welcome User  !')
else:
    print('Voce precisa ativar sua conta check seu e-mail')
"""
