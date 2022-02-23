__contas = []


def salvar_conta(conta):
    __contas.insert(1, conta)


def get_contas():
    return __contas.copy()


def buscar_contas(agencia, numero):
    for conta in __contas:
        if conta.agencia == agencia \
            and conta.numero_conta == numero:
            return conta
    return None


