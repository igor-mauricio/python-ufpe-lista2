import pytest
from src.application.Deposit import Deposit
from src.application.GetAccountInfo import GetAccountInfo
from src.application.RegisterAccount import RegisterAccount
from src.application.RegisterClient import RegisterClient
from src.infra.AccountRepository import AccountRepositoryMemory
from src.infra.ClientRepository import ClientRepositoryMemory


def test_should_deposit_money() -> None:
    clientRepository = ClientRepositoryMemory()
    accountRepository = AccountRepositoryMemory()
    registerClient = RegisterClient(clientRepository)
    registerAccount = RegisterAccount(accountRepository, clientRepository)
    getAccountInfo = GetAccountInfo(accountRepository)
    client = {
        "name": "José",
        "cpf": "12345678912"
    }
    depositAmount = 1000
    registerClient.execute(client["name"], client["cpf"])
    accountId = registerAccount.execute(client["cpf"])
    deposit = Deposit(accountRepository)
    deposit.execute(accountId, depositAmount)
    outputGetAccountInfo = getAccountInfo.execute(accountId)
    assert outputGetAccountInfo["balance"] == depositAmount
    assert outputGetAccountInfo["clientId"] == client["cpf"]
    assert outputGetAccountInfo["type"] == "Padrão"
    assert outputGetAccountInfo["id"] == accountId

def test_should_not_deposit_money_in_nonexistent_account() -> None:
    accountRepository = AccountRepositoryMemory()
    deposit = Deposit(accountRepository)
    with pytest.raises(Exception, match="Account not found"):
        deposit.execute("nonexistent_id", 1000)