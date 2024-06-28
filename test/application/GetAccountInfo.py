import pytest
from src.application.GetAccountInfo import GetAccountInfo
from src.application.RegisterAccount import RegisterAccount
from src.application.RegisterClient import RegisterClient
from src.infra.AccountRepository import AccountRepositoryMemory
from src.infra.ClientRepository import ClientRepositoryMemory


def test_shouldGetAccountsInfo() -> None:
    clientRepository = ClientRepositoryMemory()
    accountRepository = AccountRepositoryMemory()
    registerClient = RegisterClient(clientRepository)
    registerAccount = RegisterAccount(accountRepository, clientRepository)
    getAccountInfo = GetAccountInfo(accountRepository)
    client = {
        "name": "José",
        "cpf": "12345678912"
    }
    registerClient.execute(client["name"], client["cpf"])
    accountId = registerAccount.execute(client["cpf"])
    outputGetAccountInfo = getAccountInfo.execute(accountId)
    assert outputGetAccountInfo["balance"] == 0
    assert outputGetAccountInfo["clientId"] == client["cpf"]
    assert outputGetAccountInfo["type"] == "Padrão"
    assert outputGetAccountInfo["id"] == accountId

def test_shouldNotGetAccountOfInexistentClient() -> None:
    accountRepository = AccountRepositoryMemory()
    getAccountInfo = GetAccountInfo(accountRepository) 
    with pytest.raises(Exception, match="Client not found"):
        getAccountInfo.execute("12345678912")
