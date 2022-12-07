import unittest

from src.aluno.base.circulo import Circulo
from src.aluno.base.contato import Contato
from src.aluno.g_contatos import GContatos
from src.cliente.circulo_not_found_exception import CirculoNotFoundException
from src.cliente.contato_not_found_exception import ContatoNotFoundException


class ContactsCircleRelationsTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.AMIGOS = "amigos"
        cls.TRABALHO = "trabalho"
        cls.FAMILIA = "familia"
        cls.JOAQUIM_EMAIL = "joaquim@ufc.br"
        cls.JOAQUIM = "joaquim"
        cls.ANA_EMAIL = "ana@ufc.br"
        cls.ANA = "ana"
        cls.MARIO_EMAIL = "mario@ufc.br"
        cls.MARIO = "mario"
        cls.JOSE_EMAIL = "jose@ufc.br"
        cls.JOSE = "jose"
        cls.JAMES_EMAIL = "james@ufc.com"
        cls.JAMES = "james"
        cls.familia = Circulo('familia', 3)
        cls.trabalho = Circulo('trabalho', 3)
        cls.amigos = Circulo('amigos', 2)
        cls.james = Contato('james', 'james@ufc.com')
        cls.jose = Contato('jose', 'jose@ufc.br')
        cls.mario = Contato('mario', 'mario@ufc.br')
        cls.ana = Contato('ana', 'ana@ufc.br')
        cls.joaquim = Contato('joaquim', 'joaquim@ufc.br')
        cls.gcont = GContatos()

    def test_adicionarContatoCirculoExistente(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.tie(self.JAMES, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        self.assertEqual(1, self.gcont.getCircle(self.FAMILIA).getNumberOfContacts(),
                         "Numero de contatos no circulo errado")
        self.assertEqual([self.familia], self.gcont.getCircles(self.JAMES), "Lista de circulos do contato esta errada")
        self.assertEqual([self.james], self.gcont.getContacts("familia"), "Lista de contatos de um circulo esta errada")

    def test_adicionarContatoInexistenteCirculoExistente(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        with self.assertRaises(ContatoNotFoundException):
            self.gcont.tie(self.JAMES, self.FAMILIA)

        self.assertEqual(0, self.gcont.getCircle(self.FAMILIA).getNumberOfContacts(),
                         "Numero de contatos no circulo errado")

    def test_adicionarContatoCirculoInexistente(self):
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "O contato deve ser adicionado")
        with self.assertRaises(CirculoNotFoundException) as cm:
            self.gcont.tie(self.JAMES, self.FAMILIA)

        self.assertTrue(cm.getCirculoNaoEncontrado() == self.FAMILIA, "A excecao nao retornou o id do circulo que nao existe")

        self.assertEqual(self.gcont.getCircle(self.FAMILIA), None, "Circulo nao existente")
        self.assertEqual([], self.gcont.getCircles(self.JAMES), "Contato nao esta em nenhum circulo")

    def test_adicionarContatoDuplicadoCirculoExistente(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.tie(self.JAMES, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        self.assertFalse(self.gcont.tie(self.JAMES, self.FAMILIA), "Contato ja esta no circulo")
        self.assertEqual(1, self.gcont.getCircle(self.FAMILIA).getNumberOfContacts(),
                         "Numero de contatos no circulo errado")
        self.assertEqual([self.familia], self.gcont.getCircles(self.JAMES), "Lista de circulos do contato esta errada")
        self.assertEqual([self.james], self.gcont.getContacts("familia"), "Lista de contatos de um circulo esta errada")

    def test_adicionarAlemDoLimite(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")

        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.JOSE, self.JOSE_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.ANA, self.ANA_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.JOAQUIM, self.JOAQUIM_EMAIL), "O contato deve ser adicionado")

        self.assertTrue(self.gcont.tie(self.JAMES, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.JOSE, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.ANA, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        self.assertFalse(self.gcont.tie(self.JOAQUIM, self.FAMILIA), "Limite do circulo atingido")

    def test_adicionarContatoVariosCirculos(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.AMIGOS, 2), "O circulo deve ser adicionado")

        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.MARIO, self.MARIO_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.JOSE, self.JOSE_EMAIL), "O contato deve ser adicionado")

        self.assertTrue(self.gcont.tie(self.JAMES, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.MARIO, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.JOSE, self.FAMILIA), "Contato deve ser adicionado ao circulo")

        self.assertTrue(self.gcont.tie(self.JAMES, self.AMIGOS), "Contato deve ser adicionado ao circulo")

        self.assertEqual([self.amigos, self.familia], self.gcont.getCircles(self.JAMES),
                         "Lista de circulos do contato esta errada")

        self.assertEqual([self.james, self.jose, self.mario], self.gcont.getContacts(self.FAMILIA),
                         "Lista de contatos de um circulo esta errada")

    def test_removendoContatoDoCirculo(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.AMIGOS, 2), "O circulo deve ser adicionado")

        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "O contato deve ser adicionado")

        self.assertTrue(self.gcont.tie(self.JAMES, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.JAMES, self.AMIGOS), "Contato deve ser adicionado ao circulo")
        self.assertEquals([self.amigos, self.familia], self.gcont.getCircles(self.JAMES),
                          "Lista de circulos do contato esta errada")

        self.assertTrue(self.gcont.untie(self.JAMES, self.AMIGOS), "Contato deve ser removido ao circulo")

        self.assertEquals([self.familia], self.gcont.getCircles(self.JAMES), "Remocao de contato errada")

    def test_removendoContatoInexistenteDoCirculo(self):
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.tie(self.JAMES, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        with self.assertRaises(ContatoNotFoundException) as cm:
            self.gcont.untie("margarida", self.FAMILIA)

        self.assertTrue(cm.getContatoNaoEncontrado() == "margarida",
                        "A excecao nao retornou o id do contato que nao existe")
        self.assertEqual(1, self.gcont.getCircle(self.FAMILIA).getNumberOfContacts(),
                         "Numero de contatos no circulo errado")

    def test_removendoContatoDoCirculoInexistente(self):
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "O contato deve ser adicionado")
        with self.assertRaises(CirculoNotFoundException) as cm:
            self.gcont.untie(self.JAMES, self.FAMILIA)

        self.assertTrue(cm.getCirculoNaoEncontrado() == self.FAMILIA,
                        "A excecao nao retornou o id do circulo que nao existe")

    def test_removendoCirculoQuePossuiContatos(self):  # throws CirculoNotFoundException, ContatoNotFoundException {
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.AMIGOS, 2), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.TRABALHO, 3), "O circulo deve ser adicionado")

        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.MARIO, self.MARIO_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.JOSE, self.JOSE_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.ANA, self.ANA_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.JOAQUIM, self.JOAQUIM_EMAIL), "O contato deve ser adicionado")

        self.assertTrue(self.gcont.tie(self.JAMES, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.MARIO, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.JOSE, self.FAMILIA), "Contato deve ser adicionado ao circulo")

        self.assertTrue(self.gcont.tie(self.JAMES, self.TRABALHO), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.JOAQUIM, self.TRABALHO), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.ANA, self.TRABALHO), "Contato deve ser adicionado ao circulo")

        self.assertTrue(self.gcont.tie(self.JAMES, self.AMIGOS), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.removeCircle(self.FAMILIA), "O circulo deve ser removido")

        self.assertEqual([self.amigos, self.trabalho], self.gcont.getCircles(self.JAMES),
                         "Lista de circulos do contato esta errada")
        self.assertEqual([], self.gcont.getCircles(self.JOSE), "Lista de circulos do contato esta errada")
        self.assertEqual(None, self.gcont.getCircle("familia"), "Circulo nao existe mais")

    def test_removendoContatosQueEstaEmCirculos(self):  # $ throws CirculoNotFoundException, ContatoNotFoundException {

        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.AMIGOS, 2), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.TRABALHO, 3), "O circulo deve ser adicionado")

        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.JOSE, self.JOSE_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.ANA, self.ANA_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.MARIO, self.MARIO_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.JOAQUIM, self.JOAQUIM_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.tie(self.JAMES, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.MARIO, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.JOSE, self.FAMILIA), "Contato deve ser adicionado ao circulo")

        self.assertTrue(self.gcont.tie(self.JAMES, self.TRABALHO), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.JOAQUIM, self.TRABALHO), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.ANA, self.TRABALHO), "Contato deve ser adicionado ao circulo")

        self.assertTrue(self.gcont.tie(self.JAMES, self.AMIGOS), "Contato deve ser adicionado ao circulo")

        self.assertTrue(self.gcont.removeContact(self.JAMES), "O contato deve ser removido")

        self.assertEqual([self.jose, self.mario], self.gcont.getContacts("familia"),
                         "A lista de contatos do circulo esta errada")

        self.assertEqual([self.ana, self.joaquim], self.gcont.getContacts("trabalho"),
                         "A lista de contatos do circulo esta errada")

        self.assertEqual([], self.gcont.getContacts("amigos"), "A lista de contatos do circulo esta errada")

        with self.assertRaises(ContatoNotFoundException) as cm:
            self.gcont.getCircles(self.JAMES)

        self.assertTrue(cm.getContatoNaoEncontrado() == self.JAMES,
                        "A excecao nao retornou o id do contato que nao existe")

        self.assertEqual(None, self.gcont.getContact(self.JAMES))

    def test_circulosEmComum(self):  # throws CirculoNotFoundException, ContatoNotFoundException {
        self.assertTrue(self.gcont.createCircle(self.FAMILIA, 3), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.AMIGOS, 2), "O circulo deve ser adicionado")
        self.assertTrue(self.gcont.createCircle(self.TRABALHO, 3), "O circulo deve ser adicionado")

        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.MARIO, self.MARIO_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.JOSE, self.JOSE_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.ANA, self.ANA_EMAIL), "O contato deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.JOAQUIM, self.JOAQUIM_EMAIL), "O contato deve ser adicionado")

        self.assertTrue(self.gcont.tie(self.JAMES, self.FAMILIA), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.MARIO, self.FAMILIA), "Contato deve ser adicionado ao circulo")

        self.assertTrue(self.gcont.tie(self.JAMES, self.TRABALHO), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.JOAQUIM, self.TRABALHO), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.ANA, self.TRABALHO), "Contato deve ser adicionado ao circulo")

        self.assertTrue(self.gcont.tie(self.JAMES, self.AMIGOS), "Contato deve ser adicionado ao circulo")
        self.assertTrue(self.gcont.tie(self.MARIO, self.AMIGOS), "Contato deve ser adicionado ao circulo")

        self.assertEqual([self.trabalho], self.gcont.getCommomCircle(self.JAMES, self.ANA))
        self.assertEqual([], self.gcont.getCommomCircle(self.JAMES, self.JOSE))
        self.assertEqual([self.amigos, self.familia], self.gcont.getCommomCircle(self.JAMES, self.MARIO))


if __name__ == '__main__':
    unittest.main()
