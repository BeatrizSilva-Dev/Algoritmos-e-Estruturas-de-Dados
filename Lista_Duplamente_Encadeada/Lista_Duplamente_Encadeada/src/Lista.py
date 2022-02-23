class No:
    def __init__(self, elemento):
        self.elemento = elemento
        self.proximo = None


class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.__tamanho = 0

    def add_inicio(self, elemento):
        no = No(elemento)
        if self.inicio is None:
            self.inicio = no
            self.fim = no
        else:
            no.proximo = self.inicio
            self.inicio.anterior = no
            self.inicio = no
        self.__tamanho += 1

    def add_fim(self, elemento):
        no = No(elemento)
        if self.inicio is None:
            self.inicio = no
            self.inicio = no
        else:
            perc = self.inicio
            while perc.proximo is not None:
                perc = perc.proximo
            perc.proximo = no
            no.anterior = perc
            self.fim = no
        self.__tamanho += 1

    def add_index(self, i, elemento):
        if i > self.__tamanho:
            raise TypeError("Posição de memória inválida!")
        if i == self.__tamanho:
            self.add_fim(elemento)
        elif i == 0:
            self.add_inicio(elemento)
        else:
            no = No(elemento)
            perc = self.inicio
            cont = 0
            while cont < i-1:
                perc = perc.proximo
                cont += 1
            no.proximo = perc.proximo
            perc.proximo.anterior = no
            perc.proximo = no
            no.anterior = perc
            self.__tamanho += 1

    def remover_inicio(self):
        if self.inicio is None:
            raise TypeError("Lista está vazia!")
        elif self.__tamanho == 1:
            self.inicio = None
            self.fim = None
            self.__tamanho -= 1
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
            self.__tamanho -= 1

    def remover_fim(self):
        if self.inicio is None:
            raise TypeError("Lista está vazia!")
        elif self.__tamanho == 1:
            self.inicio = None
            self.fim = None
            self.__tamanho -= 1
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
            self.__tamanho -= 1

    def remover_meio(self, i):
        if self.inicio is None:
            raise TypeError("Lista está vazia!")
        elif self.__tamanho == 1:
            self.inicio = None
            self.fim = None
            self.__tamanho -= 1
        else:
            perc = self.inicio
            cont = 1
            while cont < i-1:
                perc = perc.proximo
                cont += 1
            aux = perc.proximo
            perc.proximo = aux.proximo
            aux.proximo.anterior = perc
            aux = None
            self.__tamanho -= 1

    def sobrescrever(self, index, elemento):
        perc = self.inicio
        cont = 0
        while cont != index:
            perc = perc.proximo
            cont += 1
        perc.elemento = elemento

    def get_tamanho(self):
        return self.__tamanho

    def getIndex(self, i):
        perc = self.inicio
        cont = 0
        while perc.proximo is not None:
            if cont == i:
                return perc.elemento
            perc = perc.proximo
            cont += 1

    def __str__(self):
        valor = '['
        if self.inicio is not None:
            perc = self.inicio
            valor += str(perc.elemento)
            while perc.proximo is not None:
                perc = perc.proximo
                valor += ', '
                valor += str(perc.elemento)
        valor += ']'
        return valor

    def __len__(self):
        return self.get_tamanho()

    def __getitem__(self, item):
        return self.getIndex(item)

    def __setitem__(self, key, value):
        return self.sobrescrever(key, value)
