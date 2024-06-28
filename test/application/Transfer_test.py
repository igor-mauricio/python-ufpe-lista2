import pytest
from src.application.Deposit import Deposit
from src.application.Transfer import Transfer
from src.application.GetAccountInfo import GetAccountInfo
from src.application.RegisterAccount import RegisterAccount
from src.application.RegisterClient import RegisterClient
from src.infra.AccountRepository import AccountRepositoryMemory
from src.infra.ClientRepository import ClientRepositoryMemory


def test_should_transfer_money() -> None:
    clientRepository = ClientRepositoryMemory()
    accountRepository = AccountRepositoryMemory()
    registerClient = RegisterClient(clientRepository)
    registerAccount = RegisterAccount(accountRepository, clientRepository)
    getAccountInfo = GetAccountInfo(accountRepository)
    deposit = Deposit(accountRepository)
    transfer = Transfer(accountRepository)
    sourceCpf =  "12345678912"
    destinataryCpf = "12345678913"
    startingBalance = 1000
    transferAmount = 350
    registerClient.execute("source", sourceCpf)
    registerClient.execute("destinatary", destinataryCpf)
    sourceAccountId = registerAccount.execute(sourceCpf)
    destinataryAccountId = registerAccount.execute(destinataryCpf)
    deposit.execute(sourceAccountId, startingBalance)
    transfer.execute(sourceAccountId, destinataryAccountId, transferAmount)
    outputGetAccountInfoSource = getAccountInfo.execute(sourceAccountId)
    outputGetAccountInfoDestinatary = getAccountInfo.execute(destinataryAccountId)
    assert outputGetAccountInfoSource["balance"] == 650
    assert outputGetAccountInfoDestinatary["balance"] == 350


def test_should_not_transfer_money_when_source_account_has_insufficient_balance() -> None:
    clientRepository = ClientRepositoryMemory()
    accountRepository = AccountRepositoryMemory()
    registerClient = RegisterClient(clientRepository)
    registerAccount = RegisterAccount(accountRepository, clientRepository)
    getAccountInfo = GetAccountInfo(accountRepository)
    deposit = Deposit(accountRepository)
    transfer = Transfer(accountRepository)
    sourceCpf =  "12345678912"
    destinataryCpf = "12345678913"
    startingBalance = 1000
    transferAmount = 1350
    registerClient.execute("source", sourceCpf)
    registerClient.execute("destinatary", destinataryCpf)
    sourceAccountId = registerAccount.execute(sourceCpf)
    destinataryAccountId = registerAccount.execute(destinataryCpf)
    deposit.execute(sourceAccountId, startingBalance)
    with pytest.raises(Exception, match="Saldo insuficiente"):
        transfer.execute(sourceAccountId, destinataryAccountId, transferAmount)
    outputGetAccountInfoSource = getAccountInfo.execute(sourceAccountId)
    outputGetAccountInfoDestinatary = getAccountInfo.execute(destinataryAccountId)
    assert outputGetAccountInfoSource["balance"] == 1000
    assert outputGetAccountInfoDestinatary["balance"] == 0