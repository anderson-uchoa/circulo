from abc import ABC, abstractmethod


class CirculoBase(ABC):

    def __init__(self, id: str, limite: int):
        self.id = id
        self.limite = limite

    @abstractmethod
    def setLimite(self, limite: int):
        pass

    def getId(self):
        return None

    def getLimite(self):
        return 0

    @abstractmethod
    def getNumberOfContacts(self):
        pass