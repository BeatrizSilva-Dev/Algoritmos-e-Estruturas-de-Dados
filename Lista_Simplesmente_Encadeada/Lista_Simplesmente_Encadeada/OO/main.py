
from OO import controlador_contas, controlador_admin, menu


def iniciar_sistema():
    while True:
        menu.principal()
        op = input('Digite a opção')
        if op == '0':
            print('SAIR')
            return
        elif op == '1':
            controlador_admin.iniciar_admin()
        elif op == '2':
            controlador_contas.iniciar()
        else:
            print('Opção Inválida')


iniciar_sistema()
