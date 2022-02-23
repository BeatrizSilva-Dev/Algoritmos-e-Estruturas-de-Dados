class No():
    def __init__(self,elemento):
        self.elemento = elemento
        self.inicio = None
        self.proximo = None
    def __str__(self):
        return str(self.elemento)
class Lista():
    def __init__(self):
        self.tamanho = 0
        self.inicio = None
        self.fim = None
    def __str__(self):
        perc = self.inicio
        perc = self.inicio
        valor = '['
        if perc.proximo is not None:
            valor += str(perc.elemento)
            while perc.proximo is not None:
                perc = perc.proximo
                valor += ','
                valor += str(perc.elemento)
            valor += ']'
            return valor
#1ª questão letra A
    def add_inicio(self,elemento):
        no = No(elemento)
        if self.inicio == None:
            self.inicio = no
            self.fim = no
        else:
            no.proximo = self.inicio
            self.inicio.anterior = no
            self.inicio =no
        self.tamanho += 1
    def add_fim(self,elemento):
        no = No(elemento)
        if self.inicio == None:
            self.add_inicio(elemento)
        else:
            perc = self.inicio
            while perc.proximo != None:
                perc = perc.proximo
            perc.proximo = no
            no.anterior = perc
            self.fim = no
        self.tamanho +=1
#1 questão letra B
    def add_index(self,i,elemento):
        no = No(elemento)
        if i > self.tamanho:
            raise TypeError('Posição Inválida')
        elif i == self.tamanho:
            self.add_fim(elemento)
        elif i == 0:
            self.add_inicio(elemento)
        else:
            perc = self.inicio
            cont = 1
            while cont != i:
                perc = perc.proximo
                cont +=1
            no.proximo = perc.proximo
            perc.proximo.anterior = no
            perc.proximo = no
            no.anterior = perc
            self.tamanho += 1
#letra C da 1 questão
    def remover(self,i):
        if i == 0:
            self.inicio = None
            self.fim = None
        elif self.tamanho == 1:
            self.inicio = None
            self.fim = None
        elif i == self.tamanho:
            self.fim = self.fim.anterior
            self.fim.proximo = None
        else:
            if i <= self.tamanho:
                perc = self.inicio
                cont = 1
                while cont != i:
                    perc = perc.proximo
                    cont +=1
                aux = perc.proximo
                aux.proximo.anterior = perc
                perc.proximo = aux.proximo
                aux = None
            else:
                perc = self.fim
                cont =self.tamanho
                while cont != i:
                    cont -= 1
                aux = perc.proximo
                aux.proximo.anterior = perc
                perc.proximo = aux.proximo
                aux = None
            self.tamanho -= 1