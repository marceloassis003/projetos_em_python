"""
Unittest - Antes e após kooks

---
hooks - são os testes em si. Ou seja, a execução dos testes.
---

setup() -> É executado antes de cada método de teste. É util para criarmos
instancias de objetos e outros dados:

tearDown() -> É executado ao final de cada metodo de teste. é util para excluir
dados ou fechar conexões com banco de dados.

"""
import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do setUP()
        pass

    def test_primeiro(self):
        # SetUp vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def test_segundo(self):
        # SetUp vai rodar antes do teste
        # tearDown() vai rodar após o teste.

    def tearDown(self):
        # Configurações do tearDown()
        pass





















