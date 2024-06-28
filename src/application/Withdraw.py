from dataclasses import dataclass
from src.infra.AccountRepository import AccountRepository


@dataclass
class Withdraw:
    accountRepository: AccountRepository

    def execute(self, idAccount: str, amount: float) -> None:
        account = self.accountRepository.getAccountById(idAccount)
        if not account:
            raise Exception("Account not found")
        account.withdraw(amount)
        self.accountRepository.updateAccount(account)
