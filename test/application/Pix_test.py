import pytest
from src.application.RegisterCheckingAccount import RegisterCheckingAccount
from src.application.Deposit import Deposit
from src.application.Pix import Pix
from src.application.GetAccountInfo import GetAccountInfo
from src.application.RegisterAccount import RegisterAccount
from src.application.RegisterClient import RegisterClient
from src.infra.AccountRepository import AccountRepositoryMemory
from src.infra.ClientRepository import ClientRepositoryMemory


def test_should_pix_money() -> None:
    clientRepository = ClientRepositoryMemory()
    accountRepository = AccountRepositoryMemory()
    registerClient = RegisterClient(clientRepository)
    registerCheckingAccount = RegisterCheckingAccount(accountRepository, clientRepository)
    getAccountInfo = GetAccountInfo(accountRepository)
    deposit = Deposit(accountRepository)
    pix = Pix(accountRepository)
    sourceCpf =  "12345678912"
    destinataryCpf = "12345678913"
    startingBalance = 1000
    pixAmount = 350
    registerClient.execute("source", sourceCpf)
    registerClient.execute("destinatary", destinataryCpf)
    sourceAccountId = registerCheckingAccount.execute(sourceCpf)
    destinataryAccountId = registerCheckingAccount.execute(destinataryCpf)
    deposit.execute(sourceAccountId, startingBalance)
    pix.execute(sourceAccountId, destinataryAccountId, pixAmount)
    outputGetAccountInfoSource = getAccountInfo.execute(sourceAccountId)
    outputGetAccountInfoDestinatary = getAccountInfo.execute(destinataryAccountId)
    assert outputGetAccountInfoSource["balance"] == 650
    assert outputGetAccountInfoDestinatary["balance"] == 350


def test_should_not_pix_money_when_source_account_has_insufficient_balance() -> None:
    clientRepository = ClientRepositoryMemory()
    accountRepository = AccountRepositoryMemory()
    registerClient = RegisterClient(clientRepository)
    registerCheckingAccount = RegisterCheckingAccount(accountRepository, clientRepository)
    getAccountInfo = GetAccountInfo(accountRepository)
    deposit = Deposit(accountRepository)
    pix = Pix(accountRepository)
    sourceCpf =  "12345678912"
    destinataryCpf = "12345678913"
    startingBalance = 1000
    pixAmount = 1350
    registerClient.execute("source", sourceCpf)
    registerClient.execute("destinatary", destinataryCpf)
    sourceAccountId = registerCheckingAccount.execute(sourceCpf)
    destinataryAccountId = registerCheckingAccount.execute(destinataryCpf)
    deposit.execute(sourceAccountId, startingBalance)
    with pytest.raises(Exception, match="Saldo insuficiente"):
        pix.execute(sourceAccountId, destinataryAccountId, pixAmount)
    outputGetAccountInfoSource = getAccountInfo.execute(sourceAccountId)
    outputGetAccountInfoDestinatary = getAccountInfo.execute(destinataryAccountId)
    assert outputGetAccountInfoSource["balance"] == 1000
    assert outputGetAccountInfoDestinatary["balance"] == 0


def test_should_not_pix_when_source_account_is_not_checking_account() -> None:
    clientRepository = ClientRepositoryMemory()
    accountRepository = AccountRepositoryMemory()
    registerClient = RegisterClient(clientRepository)
    registerAccount = RegisterAccount(accountRepository, clientRepository)
    getAccountInfo = GetAccountInfo(accountRepository)
    deposit = Deposit(accountRepository)
    pix = Pix(accountRepository)
    sourceCpf =  "12345678912"
    destinataryCpf = "12345678913"
    startingBalance = 1000
    pixAmount = 350
    registerClient.execute("source", sourceCpf)
    registerClient.execute("destinatary", destinataryCpf)
    sourceAccountId = registerAccount.execute(sourceCpf)
    destinataryAccountId = registerAccount.execute(destinataryCpf)
    deposit.execute(sourceAccountId, startingBalance)
    with pytest.raises(Exception, match="Conta não é corrente"):
        pix.execute(sourceAccountId, destinataryAccountId, pixAmount)
    outputGetAccountInfoSource = getAccountInfo.execute(sourceAccountId)
    outputGetAccountInfoDestinatary = getAccountInfo.execute(destinataryAccountId)
    assert outputGetAccountInfoSource["balance"] == 1000
    assert outputGetAccountInfoDestinatary["balance"] == 0