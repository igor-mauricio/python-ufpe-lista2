from abc import ABC, abstractmethod

from src.domain.Account import Account


class AccountRepository(ABC):
    @abstractmethod
    def getAccountById(self, id: str) -> Account | None:...

    @abstractmethod
    def registerAccount(self, account: Account) -> None:...

class AccountRepositoryMemory(AccountRepository):
    _accounts:list[Account] = []

    def getAccountById(self, id: str) -> Account | None:
        for account in self._accounts:
            if account.id == id:
                return account
        return None
    
    def registerAccount(self, account: Account) -> None:
        self._accounts.append(account)