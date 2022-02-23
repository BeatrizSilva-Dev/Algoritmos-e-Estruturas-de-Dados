
from OO import bd_contas, menu


def iniciar():
    print('ACESSO CAIXA ELETRONICO')
    agencia = input('DIGITE AGENCIA')
    num_conta = input('DIGITE A CONTA')
    conta = bd_contas.buscar_contas(agencia, num_conta)
    if conta is not None:
        while True:
            menu.caixa_eletronico()
            op = input('Digite a opção')
            if op == '0':
                print('SAINDO CAIXA ELETRÔNICO')
                return
            elif op == '1':
                valor = float(input('DIGITE O VALOR DE SAQUE'))
                if (conta.sacar(valor)):
                    print('SUCESSO!!!')
                else:
                    print('SALDO INDISPONÍVEL')
            elif op == '2':
                valor = float(input('DIGITE O VALOR DE SAQUE'))
                if (conta.depositar(valor)):
                    print('SUCESSO!!!')
                else:
                    print('DEPOSITO INVÁLIDO')
            elif op == '3':
                agencia = input('DIGITE AGENCIA - DESTINATÁRIO')
                num_conta = input('DIGITE A CONTA - DESTINATÁRIO')
                contas_desti = bd_contas.buscar_contas(agencia, num_conta)
                if contas_desti is not None:
                    valor = float(input('DIGITE O VALOR DE TRANSFERENCIA'))
                    if conta.transferir(valor, contas_desti):
                        print('TRANSFERENCIA COM SUCESSO')
                    else:
                        print('VALOR INDISPONÍVEL""')
                else:
                    print('CONTA DESTINATÁRIO NÃO EXISTE')



            elif op == '4':
                print(conta.get_saldo())
            else:
                print('Opção Inválida')
    else:
        print('CONTA NÃO EXISTE')
