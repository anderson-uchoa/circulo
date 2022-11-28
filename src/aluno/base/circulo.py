from src.cliente.circulo_base import CirculoBase


class Circulo(CirculoBase):

    def __init__(self, id: str, limite: int):
        super.__init__(id, limite)

    def getNumeroOfContacts(self):
        return 0


    def setLimite(self, limite: int):
        pass
