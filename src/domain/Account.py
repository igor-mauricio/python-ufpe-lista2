from __future__ import annotations
import uuid

from src.domain.Money import Money
class Account:
    def __init__(self, id: str, clientId: str, balance: Money, isCheckingAccount: bool):
        self._balance = balance
        self._clientId = clientId
        self._id = id
        self._isCheckingAccount = isCheckingAccount

    @staticmethod
    def create(clientId: str, isCheckingAccount: bool) -> Account:
        id = str(uuid.uuid4())
        balance = 0.0
        return Account(id, clientId, Money(balance), isCheckingAccount)
    
    @staticmethod
    def restore(id: str, clientId: str, balance: float, isCheckingAccount: bool) -> Account:
        return Account(id, clientId, Money(balance), isCheckingAccount)
    
    def withdraw(self, amount:float):
        if self.balance < amount:
            raise Exception("Saldo insuficiente")
        self._balance -= Money(amount)

    def deposit(self, amount:float):
        self._balance += Money(amount)
    
    def transfer(self, amount: float, account:Account):
        if self.balance < amount:
            raise Exception("Saldo insuficiente")
        self._balance -= Money(amount)
        account._balance += Money(amount)

    def pay(self, amount: float):
        if not self._isCheckingAccount:
            raise Exception("Conta não é corrente")
        self.withdraw(amount)

    def pix(self, amount: float, account:Account):
        if not self._isCheckingAccount:
            raise Exception("Conta não é corrente")
        self.transfer(amount, account)

    @property
    def id(self):
        return self._id
    
    @property
    def balance(self) -> float:
        return self._balance.value
    
    @property
    def clientId(self) -> str:
        return self._clientId
    
    @property
    def isCheckingAccount(self) -> bool:
        return self._isCheckingAccount
    
    @property
    def type(self) -> str:
        return "Corrente" if self._isCheckingAccount else "Padrão"