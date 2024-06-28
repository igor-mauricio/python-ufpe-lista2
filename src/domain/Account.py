from __future__ import annotations
import uuid
class Account:
    def __init__(self, id: str, client_id: str):
        self._saldo = 0.0
        self._client_id = client_id
        self._id = id

    @staticmethod
    def createAccount(self, client_id: str) -> Account:
        id = str(uuid.uuid4())
        return Account(id, client_id)
    
    @staticmethod
    def restoreAccount(self, id: str, client_id: str, saldo: float) -> Account:
        account = Account(id, client_id)
        account._saldo = saldo
        return account

    def getSaldo(self) -> float:
        return self._saldo
    
    def sacar(self, dinheiro:float):
        if self.getSaldo() < dinheiro:
            raise Exception("Saldo insuficiente")
        self._saldo = self.getSaldo() - dinheiro

    def depositar(self, dinheiro:float):
        if self.getSaldo() < dinheiro:
            raise Exception("Saldo insuficiente") 
        self._saldo = self.getSaldo() - dinheiro
    
    def transferencia(self, dinheiro: float, conta:Account):
        if self.getSaldo() < dinheiro:
            raise Exception("Saldo insuficiente")
        self._saldo = self.getSaldo() - dinheiro
        conta._saldo = conta.getSaldo() + dinheiro

class CheckingAccount(Account):
    _id: str

    def __init__(self, client_id: str, id: str):
        super().__init__(id, client_id)
        self._id = id   

    @staticmethod
    def createAccount(self, client_id: str) -> CheckingAccount:
        id = str(uuid.uuid4())
        return CheckingAccount(id, client_id)
    
    @staticmethod
    def restoreAccount(self, id: str, client_id: str, saldo: float) -> CheckingAccount:
        account = CheckingAccount(id, client_id)
        account._saldo = saldo
        return account

    def pagar(self, dinheiro: float):
        super().sacar(dinheiro)

    def pix(self, dinheiro: float, conta:CheckingAccount):
        super().transferencia(dinheiro, conta)