"""
Documentando funçoes com Docstrings

- podemos ter acesso a documentaçao de uma funçao em python ultilizando
a prorpriedade especial __doc__     ex -> print.__doc__

Podemos ainda fazer acesso a documentaçao com a funçao help()
"""
# exemplos

def diz_oi():
    """ Uma Funçao Simples que retorna a string 'OI !'"""
    return 'Oi !'

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrao o quadrado de 'numero' ou 'numero' a 'potencia' informada.
    :param numero: numero que desejamos gerar o exponencial.
    :param potencial: potencia que queremos gerar o exponencial . Por padrao e 2
    :return: retorne o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia







