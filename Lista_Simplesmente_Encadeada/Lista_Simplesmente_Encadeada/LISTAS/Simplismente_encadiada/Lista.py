class No:
    def __init__(self, elemento):
        self.elemento = elemento
        self.proximo = None


class Lista():
    def __init__(self):
        self.tamanho = 0
        self.inicio = None
        self.fim = None

    def __len__(self):
        return self.tamanho

    def add(self, elemento):
        no = No(elemento)
        if self.inicio is None:
            self.inicio = no
        else:
            perc = self.inicio
            while perc.proximo is not None:
                perc = perc.proximo
            perc.proximo = no
        self.tamanho += 1

        
    def inserir_inicio(self,elemento):
        no = No(elemento)
        if self.inicio is None:
            self.inicio = no
            self.fim = no
        else:
            no.proximo = self.inicio
            self.inicio = no
        self.tamanho += 1

    def inserir_fim(self,elemento):
        no = No(elemento)
        if self.inicio is None:
            self.inserir_inicio(elemento)
        else:
            self.fim.proximo = no
            self.fim = no
        self.tamanho += 1

    def inserir_meio(self,indice,elemento):
        no = No(elemento)
        if self.inicio is None:
            self.inserir_inicio(elemento)
        elif indice > (self.tamanho):
            self.inserir_fim(elemento)
        else:
            perc = self.inicio
            atual= self.inicio.proximo
            posicao = 1
            while atual != None:
                if posicao == indice:
                    perc.proximo = no
                    no.proximo = atual
                    break
                perc = atual
                atual = atual.proximo
                posicao += 1
        self.tamanho += 1
            
                

    def addI(self, indice, elemento):
        if indice > self.__tamanho:
            raise TypeError("Posição de memória inválida!")
        if indice == self.__tamanho:
            self.add_fim(elemento)
        elif indice == 0:
            self.add_inicio(elemento)
        else:
            no = No(elemento)
            perc = self.inicio
            cont = 0
            while cont < indice-1:
                perc = perc.proximo
                cont += 1
            no.proximo = perc.proximo
            perc.proximo.anterior = no
            perc.proximo = no
            no.anterior = perc
            self.__tamanho += 1

    def __str__(self):
        result = '['
        perc = self.inicio
        while perc.proximo is not None:
            result += perc.elemento + ','
            perc = perc.proximo
        result += perc.elemento + ']'
        return result
