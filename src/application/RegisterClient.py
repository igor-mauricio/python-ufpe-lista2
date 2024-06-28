from dataclasses import dataclass

from src.domain.Client import Client
from src.infra.ClientRepository import ClientRepository


@dataclass
class RegisterClient:
    clientRepository: ClientRepository

    def execute(self, name:str, cpf:str) -> None:
        client = Client.create(name, cpf)
        self.clientRepository.registerClient(client)