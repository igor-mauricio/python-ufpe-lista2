from __future__ import annotations
from dataclasses import dataclass
from typing import TypedDict

from src.domain.Account import Account
from src.infra.AccountRepository import AccountRepository
from src.infra.ClientRepository import ClientRepository


@dataclass
class GetAccountsOfClient:
    accountRepository: AccountRepository
    clientRepository: ClientRepository

    def execute(self, clientCpf: str)-> list[AccountInfo]:
        client = self.clientRepository.getClientByCpf(clientCpf)
        if not client:
            raise Exception("Client not found")
        accounts = self.accountRepository.getAccountsByCpf(clientCpf)
        return [{
            "id": account.id,
            "type": account.type,
        } for account in accounts]
    
AccountInfo = TypedDict('AccountInfo', {
    'id': str,
    'type': str
})