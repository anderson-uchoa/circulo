from abc import ABC, abstractmethod


class ContatoBase(ABC):

    def __init__(self, id:str, email:str):
        self.id = id
        self.email = email

    @abstractmethod
    def getId(self):
        pass

    @abstractmethod
    def setId(self, id:str):
        pass

    def getEmail(self):
        return None

    @abstractmethod
    def setEmail(self, email:str):
        pass

