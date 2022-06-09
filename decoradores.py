"""
Decoradores (Decorators)

o que são decorators ?

- Decorators são Funções;
- Decorators envovlvem outras funções e aprimoram seus comportamentos;
- Decorators tambem são exemplos de Higher Order Functions ;
- Decorators tem uma sisntaxe propria, usando "@" (Syntact sugar / Açucar Sintatico)


/-----------------------------------------------------\
/          Function Decorator                         \
-------------------------------------------------------

/-----------------------------------------------------\
|  | -----------------------------------------------| |
|  |        Função Decorada                        |  |
|  | -----------------------------------------------| |
|  ---------------------------------------------------

# Decoratoers como funções (Sintaxe não recomendada / Sem açucar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você ')
        funcao()
        print('Tenha um otimo dia! ')
    return sendo

def saudacao():
    print('Seja bem-vindo(a) á Geek University ')


# Testando 1

#saudacao()

teste = seja_educado(saudacao)

teste()


#   TEstando 2

def raiva():
    print('EU TE ODEIO ')

raiva_educada = seja_educado(raiva)

raiva_educada()


# Decorators com Syntax Sugar (Açucar sintatico)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você ')
        funcao()
        print('Tenha um otimo dia ! ')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro ')

# TEstando

apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero dormir...... ')

dormir()





"""
"""
|-----------------------------------------------------
| home  |    serviçoes   | produtos | administrativo |
------------------------------------------------------

http://www.suaempresa.com.br/home

http://www.suaempresa.com.br/serviços 

http://www.suaempresa.com.br/produtos 

http://www.suaempresa.com.br/admin

# Não é codigo funcional (que funcione) é apenas exemplo 

def checa_login(request):
    if not request.usuario:
        redirect ('http://www.suaempresa.com.br')
    
def home(request):
    return 'Pode Acesssar home'
     
def servicos(request):
    return 'Pode Acesssar servicos'

def produtos(request):
    return 'Pode Acesssar produtos'
    
@checa_login    
def admin(request):
    return 'Pode Acesssar admin'
    



"""
# OBS > Não confunda decorator com Decorator Function












