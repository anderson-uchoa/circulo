from abc import ABC, abstractmethod

from src.cliente.circulo_base import CirculoBase


class ICirculosManager(ABC):

    @abstractmethod
    def createCircle(self, id: str, limite: int) -> bool:
        """
        Adiciona um circulo
        Arguments:
            id do circulo: Deve ser unico
            limite: define o maximo de contatos que esse circulo pode conter
        Returns:
            true caso o contato seja adicionado, false se ja existir um circulo com o mesmo id
        """
        pass


    @abstractmethod
    def updateCircle(self, circulo: CirculoBase) -> bool:
        """
        Atualiza o limite do circulo
        Arguments:
            circulo: com o mesmo identifador e novo limite
        Returns:
            true caso o circulo seja atualizado, false se o circulo com nao existir
        """

        pass

    @abstractmethod
    def getCircle(self, idCirculo: int) -> CirculoBase:
        """
        Retorna um circulo
        Arguments:
            idCirculo: id do circulo a ser recuperado
        Returns:
            circulo caso ele exista, None se nenhum circulo com o id informado for encontrado
        """
        pass

    @abstractmethod
    def getAllCircles(self) -> list:
        """
        Retorna a lista dos circulos ordenados pelo nome

        Returns:
            a lista dos circulos ordenados pelo nome

        """
        pass

    @abstractmethod
    def removeCircle(self, idCirculo: str) -> bool:
        """
        Remove um circulo
        Arguments:
            idCirculo: identificador do circulo a ser removido
        Returns:
            true caso o circulo seja removido, false se o circulo nao existir
        """
        pass

    @abstractmethod
    def getNumberOfCircles(self) -> int:
        """
        Returns:
            o numero de circulos cadastrados
        """
        pass
