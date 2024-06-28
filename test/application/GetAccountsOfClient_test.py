import pytest
from src.application.RegisterCheckingAccount import RegisterCheckingAccount
from src.application.GetAccountsOfClient import GetAccountsOfClient
from src.application.RegisterAccount import RegisterAccount
from src.application.RegisterClient import RegisterClient
from src.infra.AccountRepository import AccountRepositoryMemory
from src.infra.ClientRepository import ClientRepositoryMemory


def test_shouldGetAccountsOfClient() -> None:
    clientRepository = ClientRepositoryMemory()
    accountRepository = AccountRepositoryMemory()
    registerClient = RegisterClient(clientRepository)
    registerAccount = RegisterAccount(accountRepository, clientRepository)
    registerCheckingAccount = RegisterCheckingAccount(accountRepository, clientRepository)
    getAccountsOfClient = GetAccountsOfClient(accountRepository, clientRepository)
    client = {
        "name": "José",
        "cpf": "12345678912"
    }
    registerClient.execute(client["name"], client["cpf"])
    accountId = registerAccount.execute(client["cpf"])
    checkingAccountId = registerCheckingAccount.execute(client["cpf"])
    outputGetAccountsOfClient = getAccountsOfClient.execute(client["cpf"])
    assert len(outputGetAccountsOfClient) == 2
    assert outputGetAccountsOfClient[0]["id"] == accountId
    assert outputGetAccountsOfClient[0]["type"] == "Padrão"
    assert outputGetAccountsOfClient[1]["id"] == checkingAccountId
    assert outputGetAccountsOfClient[1]["type"] == "Corrente"


def test_shouldNotGetAccountsOfInexistentClient() -> None:
    clientRepository = ClientRepositoryMemory()
    accountRepository = AccountRepositoryMemory()
    getAccountsOfClient = GetAccountsOfClient(accountRepository, clientRepository) 
    with pytest.raises(Exception, match="Client not found"):
        getAccountsOfClient.execute("12345678912")
