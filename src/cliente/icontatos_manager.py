from abc import ABC, abstractmethod

from src.cliente.contato_base import ContatoBase


class IContatosManager(ABC):

    @abstractmethod
    def createContact(self, id: str, email: str) -> bool:
        """
        Adiciona um contato no repositorio de contatos
        Arguments:
            id: O nome do contato. Deve ser unico
            email: O email do contato
        Returns:
            true caso o contato seja adicionado, false se um contato com o mesmo id ja existir
        """
        pass

    @abstractmethod
    def getAllContacts(self) -> list:
        """
        Retorna a lista com todos os contatos ORDENADOS POR NOME
        Returns:
            a lista de contatos
        """
        pass

    @abstractmethod
    def updateContact(self, contato: ContatoBase) -> bool:
        """
        Atualiza o email do contato idenficado pelo id
        Arguments:
            contato: Contato com o id e novo email
        Returns:
            true caso o contato seja atualizado, false se o contato com nao existir
        """
        pass


    @abstractmethod
    def removeContact(self, id: str) -> bool:
        """
        Remove um contato
        Arguments:
            id: id identificador do contato a ser removido
        Returns:
            true caso o contato seja removido, false se o contato nao existir
        """
        pass

    @abstractmethod
    def getContact(self, id: str) -> ContatoBase:
        """
        Retorna um contato
        Arguments:
            id: id do contato a ser recuperado
        Returns:
            contato caso ele exista, None se nenhum contato com o id informado for encontrado
        """
        pass

    @abstractmethod
    def getNumberOfContacts(self) -> int:
        """
        Retorna o numero de contatos cadastrados
        Returns:
            o numero de contatos
        """
        pass

    @abstractmethod
    def favoriteContact(self, idContato: str) -> bool:
        """
        Marca um contato como favorito
        Arguments:
            idContato: identificador do contato
        Returns:
            true caso o contato seja marcado, false se o contato nao existir
        """
        pass

    @abstractmethod
    def unfavoriteContact(self, idContato: str) -> bool:
        """
        Faz um contato deixar de ser favorito
        Arguments:
            idContato: identificador do contato
        Returns:
            true caso contato deixar de ser favorito, false se o contato nao existir
        """
        pass

    @abstractmethod
    def isFavorited(self, id:str) -> bool:
        """
               Verifica se um contato e favorito
               Arguments:
                   id: identificador do contato
               Returns:
                   true se o contato for favorito, false caso contrario
               """
        pass

    @abstractmethod
    def getFavorited(self) -> list:
        """
        Pega a lista de todos os favoritos
        Returns:
            a lista de favoritos
        """
        pass