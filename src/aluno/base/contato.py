from src.cliente.contato_base import ContatoBase


class Contato(ContatoBase):

    def __init__(self, id: str, email: str):
        super.__init__(id, email)


