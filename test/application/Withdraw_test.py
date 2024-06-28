import pytest
from src.application.Withdraw import Withdraw
from src.application.Deposit import Deposit
from src.application.GetAccountInfo import GetAccountInfo
from src.application.RegisterAccount import RegisterAccount
from src.application.RegisterClient import RegisterClient
from src.infra.AccountRepository import AccountRepositoryMemory
from src.infra.ClientRepository import ClientRepositoryMemory


def test_should_withdraw_money() -> None:
    clientRepository = ClientRepositoryMemory()
    accountRepository = AccountRepositoryMemory()
    registerClient = RegisterClient(clientRepository)
    registerAccount = RegisterAccount(accountRepository, clientRepository)
    getAccountInfo = GetAccountInfo(accountRepository)
    deposit = Deposit(accountRepository)
    withdraw = Withdraw(accountRepository)
    client = {
        "name": "José",
        "cpf": "12345678912"
    }
    startingBalance = 1000
    withdrawAmount = 300
    registerClient.execute(client["name"], client["cpf"])
    accountId = registerAccount.execute(client["cpf"])
    deposit.execute(accountId, startingBalance)
    withdraw.execute(accountId, withdrawAmount)
    outputGetAccountInfo = getAccountInfo.execute(accountId)
    assert outputGetAccountInfo["balance"] == 700

def test_should_not_withdraw_without_enough_money() -> None:
    clientRepository = ClientRepositoryMemory()
    accountRepository = AccountRepositoryMemory()
    registerClient = RegisterClient(clientRepository)
    registerAccount = RegisterAccount(accountRepository, clientRepository)
    getAccountInfo = GetAccountInfo(accountRepository)
    deposit = Deposit(accountRepository)
    withdraw = Withdraw(accountRepository)
    client = {
        "name": "José",
        "cpf": "12345678912"
    }
    startingBalance = 1000
    withdrawAmount = 1300
    registerClient.execute(client["name"], client["cpf"])
    accountId = registerAccount.execute(client["cpf"])
    deposit.execute(accountId, startingBalance)
    with pytest.raises(Exception, match="Saldo insuficiente"):
        withdraw.execute(accountId, withdrawAmount)
    outputGetAccountInfo = getAccountInfo.execute(accountId)
    assert outputGetAccountInfo["balance"] == 1000