import pytest
from src.domain.Account import Account


def test_should_return_the_right_type_for_account():
    checkingAccount = Account.create("12345678912", True)
    regularAccount = Account.create("12345678912", False)
    assert checkingAccount.type == "Corrente"
    assert regularAccount.type == "Padrão"

def test_should_transfer_money():
    accountSource = Account.create("12345678912", False)
    accountDestinatary = Account.create("12345678913", False)
    accountSource.deposit(1000)
    accountSource.transfer(350, accountDestinatary)
    assert accountSource.balance == 650
    assert accountDestinatary.balance == 350

def test_should_not_transfer_money_when_source_account_has_insufficient_balance():
    accountSource = Account.create("12345678912", False)
    accountDestinatary = Account.create("12345678913", False)
    accountSource.deposit(1000)
    with pytest.raises(Exception, match="Saldo insuficiente"):
        accountSource.transfer(1100, accountDestinatary)

def test_should_pix_money():
    accountSource = Account.create("12345678912", True)
    accountDestinatary = Account.create("12345678913", True)
    accountSource.deposit(1000)
    accountSource.pix(350, accountDestinatary)
    assert accountSource.balance == 650
    assert accountDestinatary.balance == 350

def test_should_not_pix_money_when_source_account_has_insufficient_balance():
    accountSource = Account.create("12345678912", True)
    accountDestinatary = Account.create("12345678913", True)
    accountSource.deposit(1000)
    with pytest.raises(Exception, match="Saldo insuficiente"):
        accountSource.pix(1100, accountDestinatary)
    assert accountSource.balance == 1000
    assert accountDestinatary.balance == 0

def test_should_not_pix_money_when_source_account_is_not_checking_account():
    accountSource = Account.create("12345678912", False)
    accountDestinatary = Account.create("12345678913", False)
    accountSource.deposit(1000)
    with pytest.raises(Exception, match="Conta não é corrente"):
        accountSource.pix(350, accountDestinatary)
    assert accountSource.balance == 1000
    assert accountDestinatary.balance == 0

def test_should_withdraw_money():
    account = Account.create("12345678912", False)
    account.deposit(1000)
    account.withdraw(350)
    assert account.balance == 650

def test_should_not_withdraw_money_when_balance_is_insufficient():
    account = Account.create("12345678912", False)
    account.deposit(1000)
    with pytest.raises(Exception, match="Saldo insuficiente"):
        account.withdraw(1100)
    assert account.balance == 1000

def test_should_not_pay_when_account_is_not_checking_account():
    account = Account.create("12345678912", False)
    account.deposit(1000)
    with pytest.raises(Exception, match="Conta não é corrente"):
        account.pay(350)
    assert account.balance == 1000

def test_should_pay():
    account = Account.create("12345678912", True)
    account.deposit(1000)
    account.pay(350)
    assert account.balance == 650

def test_should_not_pay_money_when_account_is_not_checking_account():
    accountSource = Account.create("12345678912", False)
    accountSource.deposit(1000)
    with pytest.raises(Exception, match="Conta não é corrente"):
        accountSource.pay(350)
    assert accountSource.balance == 1000

def test_should_deposit_money():
    account = Account.create("12345678912", False)
    account.deposit(1000)
    assert account.balance == 1000