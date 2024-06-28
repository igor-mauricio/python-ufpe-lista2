from __future__ import annotations
from dataclasses import dataclass
from typing import TypedDict

from src.domain.Account import Account
from src.infra.AccountRepository import AccountRepository


@dataclass
class GetAccountInfo:
    accountRepository: AccountRepository

    def execute(self, accountId: str) -> Output:
        account = self.accountRepository.getAccountById(accountId)
        if not account:
            raise Exception("Account not found")
        return {
            "id": account.id,
            "balance": account.balance,
            "clientId": account.clientId,
            "type": account.type,
        }
    
Output = TypedDict('Output', {
    'id': str,
    'balance': float,
    'clientId': str,
    "type": str
})