import unittest

from src.aluno.base.circulo import Circulo
from src.aluno.g_contatos import GContatos


class CircleTests(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.AMIGOS = "amigos"
        cls.TRABALHO = "trabalho"
        cls.FAMILIA = "familia"

        cls.familia = Circulo('familia', 3)
        cls.trabalho = Circulo('trabalho', 3)
        cls.amigos = Circulo('amigos', 1)
        cls.gcont = GContatos()

    def test_adicionarCirculos(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.AMIGOS, 1), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.TRABALHO, 3), "O circulo deve ser adicionado")

        self.assertEqual(3, self.gcont.getNumberOfCircles(), "Todos os 3 circulos devem ser adiconados")

    def test_adicionarCirculoLimiteInvalido(self):
        self.assertTrue(self.gcont.createCircle(self.TRABALHO, 3), "O circulo deve ser adicionado")
        self.assertFalse(self.gcont.createCircle(self.TRABALHO, -5),
                         "Circulo com limite menor ou igual a zero nao deve ser adicionado")

        self.assertEqual(1, self.gcont.getNumberOfCircles(), "Apenas um ciruclo devia ter sido adicionado")

    def test_adicionarCirculoDuplicado(self):
        self.assertTrue(self.gcont.createCircle(self.TRABALHO, 3), "O circulo deve ser adicionado")
        self.assertFalse(self.gcont.createCircle(self.TRABALHO, 5), "Circulo com id duplicado nao deve ser adicionado")

        self.assertEqual(1, self.gcont.getNumberOfCircles(), "Apenas um ciruclo devia ter sido adicionado")

    def test_buscandoCirculoExistente(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertEqual(self.gcont.getCircle(self.FAMILIA), self.familia, "O circulo recuperado nao foi procurado")

    def test_buscandoCirculoInexistente(self):
        self.assertEqual(self.gcont.getCircle("inimigos"), None, "Circulo nao existente")

    def test_recuperandoTodosOsCirculos(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.AMIGOS, 1), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.TRABALHO, 3), "O circulo deve ser adicionado")

        self.assertEqual([self.amigos, self.familia, self.trabalho], self.gcont.getAllCircles(),
                         "Lista de circulos incorreta")

    def test_removendoCirculoExistente(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.AMIGOS, 1), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.TRABALHO, 3), "O circulo deve ser adicionado")

        self.assertTrue(self.gcont.removeCircle(self.AMIGOS), "Circulo nao removido")
        self.assertEqual(2, self.gcont.getNumberOfCircles(), "Quantidade de circulos errada")
        self.assertEqual([self.familia, self.trabalho], self.gcont.getAllCircles(), "Lista de circulos incorreta")

    def test_removendoCirculoInexistente(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.AMIGOS, 1), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.TRABALHO, 3), "O circulo deve ser adicionado")

        self.assertFalse(self.gcont.removeCircle("inimigos"), "Circulo nao existe, logo nao pode ser removido")
        self.assertEqual(3, self.gcont.getNumberOfCircles(), "Quantidade de circulos errada")
        self.assertEqual([self.amigos, self.familia, self.trabalho], self.gcont.getAllCircles(),
                         "Lista de circulos incorreta")

    def test_atualizandoCirculoExistente(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.updateCircle(Circulo(self.FAMILIA, 4)), "O circulo deve ser atualizado")
        self.assertEqual(self.gcont.getCircle(self.FAMILIA), Circulo(self.FAMILIA, 4),
                         "O circulo nao foi atualizado corretamente")

    def test_atualizandoCirculoLimiteInvalido(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertFalse(self.gcont.updateCircle(Circulo(self.FAMILIA, 0)), "O circulo possui limite invalido")

    def test_atualizandoCirculoInexistente(self):
        self.assertFalse(self.gcont.updateCircle(Circulo("inimigos", 4)), "Circulo nao existente")
        self.assertEqual(self.gcont.getCircle(self.FAMILIA), None, "Circulo nao foi cadastrado")


if __name__ == '__main__':
    unittest.main()
