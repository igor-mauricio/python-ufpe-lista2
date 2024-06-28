from abc import ABC, abstractmethod

from src.domain.Client import Client


class ClientRepository(ABC):
    @abstractmethod
    def getClientByCpf(self, cpf: str) -> Client | None:...

    @abstractmethod
    def registerClient(self, client: Client) -> None:...

class ClientRepositoryMemory(ClientRepository):
    _clients:list[Client]

    def __init__(self):
        self._clients = []

    def getClientByCpf(self, cpf: str) -> Client | None:
        for client in self._clients:
            if client.cpf == cpf:
                return client
        return None
    
    def registerClient(self, client: Client) -> None:
        self._clients.append(client)