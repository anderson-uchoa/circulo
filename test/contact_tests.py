import unittest

from src.aluno.base.contato import Contato
from src.aluno.g_contatos import GContatos


class ContactTests(unittest.TestCase):

    @classmethod
    def setUp(cls):
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
        cls.james = Contato('james', 'james@ufc.com')
        cls.jose = Contato('jose', 'jose@ufc.br')
        cls.mario = Contato('mario', 'mario@ufc.br')
        cls.ana = Contato('ana', 'ana@ufc.br')
        cls.joaquim = Contato('joaquim', 'joaquim@ufc.br')

        cls.gcont = GContatos()

    def test_adicionarContato(self):
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "Contato valido, deve ser adicionado")
        self.assertEqual(1, self.gcont.getNumberOfContacts(), "Quantidade de contatos errada")

    def test_adicionarContatoDuplicado(self):
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "Contato valido, deve ser adicionado")
        self.assertFalse(self.gcont.createContact(self.JAMES, "jesus2@ufc.com"), "Contato com id duplicado")
        self.assertEqual(1, self.gcont.getNumberOfContacts(), "Quantidade de contatos errada")

    def test_removendoContato(self):
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "Contato valido, deve ser adicionado")
        self.assertEqual(1, self.gcont.getNumberOfContacts(), "Quantidade de contatos errada")
        self.assertTrue(self.gcont.removeContact(self.JAMES), "Contato deve ser removido")
        self.assertEqual(0, self.gcont.getNumberOfContacts(), "Quantidade de contatos errada")

    def test_removendoContatoInexistente(self):
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "Contato valido, deve ser adicionado")
        self.assertEqual(1, self.gcont.getNumberOfContacts(), "Quantidade de contatos errada")
        self.assertFalse(self.gcont.removeContact("ramiro"), "Contato nao cadastrado nao pode ser removido")
        self.assertEqual(1, self.gcont.getNumberOfContacts(), "Quantidade de contatos errada")

    def test_recuperandoContato(self):
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "Contato valido, deve ser adicionado")
        self.assertEqual(1, self.gcont.getNumberOfContacts(), "Quantidade de contatos errada")
        james = self.gcont.getContact(self.JAMES)
        self.assertEqual(james, self.james, "Contato recuperado diferente do buscado")

    def test_recuperandoContatoInexistente(self):
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "Contato valido, deve ser adicionado")
        self.assertEqual(1, self.gcont.getNumberOfContacts(), "Quantidade de contatos errada")
        self.assertEqual(None, self.gcont.getContact("ramiro"), "Contato nao existente")

    def test_recuperandoTodosOsContatos(self):
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "Contato valido, deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.ANA, self.ANA_EMAIL), "Contato valido, deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.JOSE, self.JOSE_EMAIL), "Contato valido, deve ser adicionado")

        self.assertEqual([self.ana, self.james, self.jose], self.gcont.getAllContacts(), "Lista de contatos errada")

    def test_atualizandoContato(self):
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "Contato valido, deve ser adicionado")
        self.assertEqual(1, self.gcont.getNumberOfContacts(), "Quantidade de contatos errada")

        self.james.setEmail("novo@ufc.br")

        self.assertTrue(self.gcont.updateContact(self.james), "Contato valido, deve ser atualizado")
        james = self.gcont.getContact(self.JAMES)
        self.assertEqual(james, self.james, "Contato nao foi atualizado corretamente")

    def test_atualizandoInexistente(self):
        self.assertFalse(self.gcont.updateContact(self.james), "Contato nao existente, logo nao pode ser atualizado")

    def test_favoritandoUmContato(self):
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "Contato valido, deve ser adicionado")
        self.assertTrue(self.gcont.favoriteContact(self.JAMES), "Contato deve ser marcado como favorito")
        self.assertTrue(self.gcont.isFavorited(self.JAMES), "Contato esta na lista de favoritos")
        self.assertFalse(self.gcont.isFavorited(self.ANA), "Contato nao esta na lista de favoritos")

    def test_favoritandoUmContatoInexistente(self):
        self.assertFalse(self.gcont.favoriteContact(self.JAMES), "Contato nao existe")
        self.assertFalse(self.gcont.isFavorited(self.JAMES), "Contato nao esta na lista de favoritos")

    def test_desfavoritandoUmContato(self):
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "Contato valido, deve ser adicionado")
        self.assertTrue(self.gcont.favoriteContact(self.JAMES), "Contato deve ser marcado como favorito")
        self.assertTrue(self.gcont.isFavorited(self.JAMES), "Contato esta na lista de favoritos")

        self.assertTrue(self.gcont.unfavoriteContact(self.JAMES), "Contato nao removido dos favoritos")
        self.assertFalse(self.gcont.isFavorited(self.JAMES), "Contato nao esta na lista de favoritos")

    def test_desfavoritandoUmContatoInexistente(self):
        self.assertFalse(self.gcont.unfavoriteContact(self.JAMES), "Contato nao existe")
        self.assertFalse(self.gcont.isFavorited(self.JAMES), "Contato nao esta na lista de favoritos")

    def test_recuperandoTodosOsFavoritos(self):
        self.assertTrue(self.gcont.createContact(self.JAMES, self.JAMES_EMAIL), "Contato valido, deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.MARIO, self.MARIO_EMAIL), "Contato valido, deve ser adicionado")
        self.assertTrue(self.gcont.createContact(self.ANA, self.ANA_EMAIL), "Contato valido, deve ser adicionado")

        self.assertTrue(self.gcont.favoriteContact(self.JAMES), "Contato deve ser marcado como favorito")
        self.assertTrue(self.gcont.favoriteContact(self.ANA), "Contato deve ser marcado como favorito")
        self.assertTrue(self.gcont.favoriteContact(self.MARIO), "Contato deve ser marcado como favorito")

        self.assertTrue(self.gcont.isFavorited(self.ANA), "O contato esta na lista de favoritos")
        self.assertFalse(self.gcont.isFavorited(self.JOSE), "O contato nao esta na lista de favoritos")

        self.assertEqual([self.ana, self.james, self.mario], self.gcont.getFavorited(), "Lista de favoritos errada")

        self.assertTrue(self.gcont.unfavoriteContact(self.ANA), "Contato deve ser removido dos favoritos")

        self.assertEqual([self.james, self.mario], self.gcont.getFavorited(), "Remocao de favoritos errada")

        self.assertTrue(self.gcont.removeContact(self.MARIO), "Contato deve ser removido dos favoritos")

        self.assertEqual([self.james], self.gcont.getFavorited(), "Remocao de favoritos errada")


if __name__ == '__main__':
    unittest.main()
