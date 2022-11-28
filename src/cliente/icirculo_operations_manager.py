from abc import ABC, abstractmethod


class ICirculoOperationsManager(ABC):

    @abstractmethod
    def tie(self,idContato: str, idCirculo: str) -> bool:
        """
        Adiciona um contato a um circulo
        Arguments:
            idContato: identificao do contato
            idCirculo: identificao do do circulo
        Returns:
            true se o contato for adicionado ao circulo false se o circulo ja estiver cheio
        Raises:
            CirculoNotFoundException:
                caso o circulo informado nao exista
            ContatoNotFoundException:
                caso o contato informado nao exista
        """
        pass


    @abstractmethod
    def untie(self,idContato: str, idCirculo: str) -> bool:
        """
        Remove um contato de um circulo
        Arguments:
            idContato: identificao do contato
            idCirculo: identificao do circulo
        Returns:
            true caso o contato seja removido, false se o contato nao estiver contido no circulo
        Raises:
            CirculoNotFoundException:
                caso o circulo informado nao exista
            ContatoNotFoundException:
                caso o contato informado nao exista
        """
        pass


    @abstractmethod
    def getContacts(self, id:str) -> list:
        """
        Retorna a lista de contatos ordenas por nome contido em um circulo
        Arguments:
            id: do circulo
        Returns:
            a lista de contato contido no circulo ordenado pelo nome
        Raises:
            ContatoNotFoundException:
                caso o contato informado nao exista
        """
        pass



    @abstractmethod
    def getCircles(self, id: str) -> list:
        """
        Retorna a lista de circulos cujo o contato pertence
        Arguments:
            id: do contato
        Returns:
            a lista de circulo que contem o contato ordenado pelo nome
        Raises:
            ContatoNotFoundException:
                caso o contato informado nao exista
        """
        pass


    @abstractmethod
    def getCommomCircle(self, idContato1: str, idContato2: str)-> list:
        """
        Retorna a lista de circulo ordenados pelo nome que os dois contatos possuem em comum
        Arguments:
            idContato1: identificador de um contato
            idContato2: identificador do outro contato
        Returns:
            a lista de circulos em comum ordenados pelo nome
        Raises:
            ContatoNotFoundException:
                caso algum dos contatos nao existam

           """
        pass