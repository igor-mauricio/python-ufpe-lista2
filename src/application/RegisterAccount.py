from dataclasses import dataclass

from src.domain.Account import Account
from src.infra.AccountRepository import AccountRepository
from src.infra.ClientRepository import ClientRepository


@dataclass
class RegisterAccount:
    accountRepository: AccountRepository
    clientRepository: ClientRepository

    def execute(self, clientCpf: str) -> str:
        client = self.clientRepository.getClientByCpf(clientCpf)
        if not client:
            raise Exception("Client not found")
        account = Account.create(clientCpf, isCheckingAccount=False)
        self.accountRepository.registerAccount(account)
        return  account.id