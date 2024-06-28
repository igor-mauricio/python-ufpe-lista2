from abc import ABC, abstractmethod

from src.domain.Account import Account


class AccountRepository(ABC):
    @abstractmethod
    def getAccountById(self, id: str) -> Account | None:...

    @abstractmethod
    def getAccountsByCpf(self, cpf: str) -> list[Account]:...

    @abstractmethod
    def registerAccount(self, account: Account) -> None:...

    @abstractmethod
    def updateAccount(self, account: Account) -> None:...

class AccountRepositoryMemory(AccountRepository):
    _accounts:list[Account]

    def __init__(self):
        self._accounts = []

    def getAccountById(self, id: str) -> Account | None:
        for account in self._accounts:
            if account.id == id:
                return account
        return None
    
    def getAccountsByCpf(self, cpf: str) -> list[Account]:
        return [account for account in self._accounts if account.clientId == cpf]
    
    def registerAccount(self, account: Account) -> None:
        self._accounts.append(account)

    def updateAccount(self, account: Account) -> None:
        for i in range(len(self._accounts)):
            if self._accounts[i].id == account.id:
                self._accounts[i] = account
                return
        raise Exception("Account not found")