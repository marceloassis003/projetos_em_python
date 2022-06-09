"""
POO - Classes

Em POO, Classes nada mais são do que objetos do mundo real sendo representados
computacionalmente.

Imagine que voce queira fazer um sistema para automatizar o controle das lampadas
da sua casa.

Classes podem conter:
    - Atributos -> Representam as caracteristicas do objeto, ou seja, pelos atributos
    conseguimos representar computacionalmente os estados de um objeto. No caso da lampada,
    possivelmente iriamos querer saber se a lampada é 110 ou 220 volts, se ela é branca,
    amarela, vermelha ou outra cor, qual é a luminosidade dela e etc.

    - Métodos (funções) -> Representam os comportamentos do objeto , ou seja, as ações que este
    objeto pode realizar no seu sistema. No caso da lãmpada, por exemplo, um comportamento comum
    que muito provavelmente iriamos querer representar no nosso sistema é o de ligar e desligar
    a mesma.

Em python, para definir uma classe ultlizamos a palavra Class.

Ultlizamos a palavra 'pass' em python quando temos um bloco de codigo que ainda não esta
implementado.

Quando nomeamos nossas classes em python ultlizamos por convenção o nome com inicial
em maiusculo. Se o nome for composto, ultliza-se as iniciais de ambas as palavras em
maiúsculo, todas juntas.

DICA: Em computação não ultlizamos acentuação, caracteres especiais, espaços ou similares
para nome de classes, atributos, métodos, arquivos, diretóriose etc.

Quando estamos planejando um software e definimos quais classes teremos que ter no sistema,
chamamos estes objetos que serão mapeados para classes de entidade.
"""

class Lampada:
    pass

class ContaCorrente:
    pass

class Produto:
    pass

class Usuario:
    pass

class Int:
    pass

lamp = Lampada()

print(type(lamp))


print(help(int))

inteiro = Int()






















