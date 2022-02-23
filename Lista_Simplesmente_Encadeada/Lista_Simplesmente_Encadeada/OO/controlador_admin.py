
from OO import bd_contas, menu
from OO.classes import Conta


def iniciar_admin():
    while True:
        menu.admin()
        op = input('Digite a opção')
        if op == '0':
            print('SAIR')
            return
        elif op == '1':
            cadastrar()
        elif op == '2':
            listar_todos()
        elif op == '3':
            pass
        else:
            print('Opção Inválida')


def cadastrar():
    cpf = input('DIGITE O CPF')
    agencia = input('DIGITE o agencia')
    num_conta = input('DIGITE o numero da conta')
    conta = Conta(cpf, agencia, num_conta)
    bd_contas.salvar_conta(conta)


def listar_todos():
    contas = bd_contas.get_contas()
    for conta in contas:
        print(conta)
