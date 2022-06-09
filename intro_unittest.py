"""
Introdução ao módulo Unittest

Unittest -> Testes Unitarios

O que são testes unitarios?

Teste é a forma de se testar unidades individuais de codigo fonte.

Unidades individuais podem ser: Funções, metodos, classes, módulos etc.

#OBS: Teste unitario não é especifico da linguagem python.

Para criar nossos testes, criamos classes que herdam de unittest. TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes. Ultlizamos unittest.main()

TesteCase -> Casos de testes para sua unidade.

# Conhecendo as assertions

Método                       checa que
assertEquals(a, b)              a == b
assertNotEquals(a, b)           a != b
assertTrue(x)                   x é verdadeiro
assertFalse(x)                  x é falso
assertIs(a, b)                  a é b
assertIsNot(a, b)               a não é b
assertIsNone(x)                 x é none
assertIsNotNone(x)              x não é none
assertIn(a, b)                  a esta em b
assertNotIn(a, b)               a não esta em b
assertIsInstance(a, b)          a é instancia de b
assertNotIsInstance(a, b)       a não é instancia de b


Por comvenção todos os testes em um test case, devem ter
seu nome iniciado com test_

# Para executar os testes com unitest

python nome_do_modulo.py

# para executar os testes com unittest no modo  verbose

python nome_do_modulo -v

Podemos acrescentar (e é recomendado) docstring nos nossos testes.
"""

# Prática - Ultlizando a abordagem TDD















