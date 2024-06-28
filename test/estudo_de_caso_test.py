import pytest
from src.domain.Client import Client
from src.domain.Money import Money
from src.estudo_de_caso import ContaCorrente


def test_deve_dar_erro_quando_tenta_sacar_sem_dinheiro()-> None:
    cliente = Client("Igor", "123")
    id = "1234"
    valor = Money(10)

    conta_corrente = ContaCorrente(cliente, id)

    with pytest.raises(Exception, match='Saldo insuficiente'):
        conta_corrente.sacar(valor)


def test_sacar_quando_tenta_sacar_com_dinheiro()-> None:
    cliente = Client("Rebeka", "123")
    id = "1234"
    saldo_inicial = Money(1000)
    valor = Money(10)

    conta_corrente = ContaCorrente(cliente, id)
    conta_corrente.depositar(saldo_inicial)

    conta_corrente.sacar(valor)

    esperado = Money(990)

    assert conta_corrente.getSaldo() == esperado


def test_deve_transferir_com_dinheiro()-> None:
    cliente = Client("Rebeka", "123")
    id = "1234"
    saldo_inicial = Money(1000)

    cliente2 = Client("Igor", "124")
    id2 = "1235"
    saldo_inicial2 = Money(50)


    valor_transferencia = Money(200)

    conta_corrente_1 = ContaCorrente(cliente, id)
    conta_corrente_1.depositar(saldo_inicial)

    conta_corrente_2 = ContaCorrente(cliente2, id2)
    conta_corrente_2.depositar(saldo_inicial2)

    conta_corrente_1.transferencia(valor_transferencia, conta_corrente_2)

    esperado_conta_corrente_1 = Money(800)
    esperado_conta_corrente_2 = Money(250)

    assert conta_corrente_1.getSaldo() == esperado_conta_corrente_1
    assert conta_corrente_2.getSaldo() == esperado_conta_corrente_2

def test_nao_deve_transferir_sem_dinheiro()-> None:
    cliente = Client("Rebeka", "123")
    id = "1234"
    saldo_inicial = Money(1000)

    cliente2 = Client("Igor", "124")
    id2 = "1235"
    saldo_inicial2 = Money(50)


    valor_transferencia = Money(2000)

    conta_corrente_1 = ContaCorrente(cliente, id)
    conta_corrente_1.depositar(saldo_inicial)

    conta_corrente_2 = ContaCorrente(cliente2, id2)
    conta_corrente_2.depositar(saldo_inicial2)

    
    with pytest.raises(Exception, match='Saldo insuficiente'):
        conta_corrente_1.transferencia(valor_transferencia, conta_corrente_2)

    esperado_conta_corrente_1 = Money(1000)
    esperado_conta_corrente_2 = Money(50)

    assert conta_corrente_1.getSaldo() == esperado_conta_corrente_1
    assert conta_corrente_2.getSaldo() == esperado_conta_corrente_2

    