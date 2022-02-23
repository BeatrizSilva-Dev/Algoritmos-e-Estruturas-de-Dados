import datetime


class Conta():
    def __init__(self, cpf, agencia, numero_conta):
        self.cpf = cpf
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.__saldo = 100.00

    def sacar(self, valor):
        if self.__saldo < valor:
            return False
        self.__saldo -= valor
        return True

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def get_saldo(self):
        return self.__saldo

    def transferir(self, valor, contaDestino):
        if self.sacar(valor):
            contaDestino.depositar(valor)
            return True
        return False

    def __str__(self):
        return 'CPF: {} - Conta: {}'.format(self.cpf, self.numero_conta)

