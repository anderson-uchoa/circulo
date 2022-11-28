from src.cliente.exception_base import ExceptionBase


class ContatoNotFoundException  (ExceptionBase):


    def __init__(self, contatoId: str, message="Circulo não encontrado"):
        self.contatoId = contatoId
        super.__init__(message)

    def getContatoNaoEncontrado(self):
        return None