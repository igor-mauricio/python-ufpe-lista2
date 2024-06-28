from dataclasses import dataclass
from src.infra.AccountRepository import AccountRepository


@dataclass
class Pix:
    accountRepository: AccountRepository

    def execute(self, idSourceAccount: str, idDestinationAccount: str, amount: float) -> None:
        sourceAccount = self.accountRepository.getAccountById(idSourceAccount)
        if not sourceAccount:
            raise Exception("Account not found")
        destinationAccount = self.accountRepository.getAccountById(idDestinationAccount)
        if not destinationAccount:
            raise Exception("Account not found")
        sourceAccount.pix(amount, destinationAccount)
        self.accountRepository.updateAccount(sourceAccount)
        self.accountRepository.updateAccount(destinationAccount)