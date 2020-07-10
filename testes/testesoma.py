import unittest
from src.main import soma


class TestSoma(unittest.TestCase):
    def teste_retorno_soma_10_10(self):
        self.assertEqual(soma(10, 10), 20)

    def teste_retorno_soma_20_10(self):
        self.assertEqual(soma(20, 10), 30)
