class No():
    def __init__(self, elemento):
        self.elemento = elemento
        self.esquerda = None
        self.direita = None
        self.valor = None
        self.pai = None
        self.atualizaBalanceamento = 0


    def __str__(self):
        return str(self.elemento)

class Arvore():
    def __init__(self):
        self.raiz = None
        self.__quantFolhas = 0
        #self.nivel = 0

    def add(self, elemento):
        no = No(elemento)
        perc = self.raiz
        if self.raiz == None:
            self.raiz = no
        else:
            while True:
                if no.elemento > perc.elemento:
                    if perc.direita != None:
                        perc = perc.direita
                    else:
                        perc.direita = no
                        self.atualizaBalanceamento(no)
                        break
                elif no.elemento < perc.elemento:
                    if perc.esquerda != None:
                        perc = perc.esquerda
                    else:
                        perc.esquerda = no
                        self.atualizaBalanceamento(no)
                        break
                else:
                    raise Exception("Elemento já adicionado na lista")

        self.__quantFolhas += 1

    def getTamanho(self):
        return self.__quantFolhas

    def imprimirNo(self, no):
        if no != None:
            self.imprimirNo(no.esquerda)
            print(no, end='-')
            self.imprimirNo(no.direita)
    def imprimir(self):
        return self.imprimirNo(self.raiz)



    def min(self, no):
        perc= no
        if perc == None:
            ValueError('Não existe')
        else:
            while perc.esquerda != None:
                perc = perc.esquerda
            return perc
    def max(self,no):
        perc = no
        if perc == None:
            ValueError('Não existe')
        else:
            while perc.direita != None:
                perc = perc.direita
            return perc
    def sucessor(self,no):
        if no is None:
            no = self.raiz
        return  self.min(no.direita)
    def predecessor(self,no):
        if no is None:
            no = self.raiz
        return self.max(no.esquerda)
    def buscarInt(self,elemento,pai,pos,perc):
        if perc != None:
            if perc.elemento == elemento:
                if pai == perc:
                    pos = 'CENTRAL'
                return pai,pos,perc
            elif elemento < perc.elemento:
                return self.buscarInt(elemento,perc,'ESQ',perc.esquerda)
            else:
                return self.buscarInt(elemento,perc,'DIR',perc.direita)
        else:
            raise RecursionError('algo errado não está certo')
    def buscar_(self,elemento):
        return self.buscarInt(elemento,self.raiz,'',self.raiz)

    def buscar(self, no, valor):
        if no != None:
            if no.elemento == valor:
                return no
            elif valor <= no.elemento:
                return self.buscar(no.esquerda, valor)
            else:
                return self.buscar(no.direita, valor)
        raise ValueError('Não existe')
    def remover(self,elemento):
        if self.raiz == None:
            raise ValueError('A raiz está vazia')
        perc = self.raiz
        pai = perc
        percEsquerdo = True
        while perc.elemento != elemento:
            pai = perc
            if perc.elemento > elemento:
                perc = perc.esquerda
                percEsquerdo = True
            else:
                perc = perc.direita
                percEsquerdo = False
            if perc == None:
                return False
        if perc.esquerda == None and perc.direita == None:
            if perc == self.raiz:
                self.raiz = None
            else:
                if percEsquerdo:
                    pai.esquerda = None
                else:
                    pai.direita = None
        elif perc.direita == None:
            if perc == self.raiz:
                self.raiz = perc.esquerda
            else:
                if percEsquerdo:
                    pai.esquerda = perc.esquerda
                else:
                    pai.direita = perc.esquerda
                perc = None
        elif perc.esquerda == None:
            if perc == self.raiz:
                self.raiz = perc.direita
            else:
                if percEsquerdo:
                    pai.esquerda = perc.direita
                else:
                    pai.direita = perc.direita
                perc = None
        else:
            novo = self.sucessor(perc)
            if perc == self.raiz:
                self.raiz = novo
            else:
                if percEsquerdo:
                    pai.esquerda = novo
                else:
                    pai.direita = novo
            novo.esquerda = perc.esquerda
            perc = None
        return True
    def ListaremOrdem(self, perc):
        if perc != None:
            self.ListaremOrdem(perc.esquerda)
            print(perc.elemento, end=" ")
            self.ListaremOrdem(perc.direita)

    def altura(self, perc):
        if perc == None or perc.esquerda== None and perc.direita == None:
            return -1
        else:
            alturaEsquerda = self.altura(perc.esquerda)
            alturaDireita = self.altura(perc.direita)
            return max(alturaEsquerda,alturaDireita) + 1
    def folhas(self, perc):
        if perc == None:
            return 0
        if perc.esquerda == None and perc.direita == None:
            return 1
        return self.folhas(perc.esquerda) + self.folhas(perc.direita)

    def contarNos(self, perc):
        if perc == None:
            return 0
        else:
            return 1 + self.contarNos(perc.esquerda) + self.contarNos(perc.direita)
    def total_de_elementos_nó(self,elemento):
        pai,pos,perc = self.buscar_(elemento)
        if perc.esquerda == None and perc.direita == None:
            return print('não há filhos')
        elif perc.esquerda == None and perc.direita != None or perc.direita == None and perc.esquerda != None:
            return print('há um filho')
        else:
            return print('há dois filhos')
    def nível_de_cada_elemento(self,elemento,cont):
        if self.raiz == None:
            raise ('Raiz vazia')
        perc = self.raiz
        pai = self.raiz
        while perc.elemento != elemento:
            pai = perc
            if elemento < perc.elemento:
                perc = perc.esquerda
                cont += 1
            else:
                perc = perc.direita
                cont += 1
        while perc.elemento == elemento:
            return cont
    def retornar_nível(self,elemento):
        #pai,pos,perc = self.buscar_(elemento)
        pass
    def rotacaoEsquerda(self,no):
        novo = no.direita
        aux = novo.esquerda
        novo.esquerda = no
        no.direita = aux
        if(self.raiz == no):
            self.raiz = novo
            no.pai = novo
            novo.pai = None
        else:
            no.pai.direita = novo
            novo.pai = no.pai
            no.pai = novo
        self.atualizaBalanceamento(novo)
        self.atualizaBalanceamento(no)

    def rotacaoDireita(self,no):
        nova = no.esquerda
        aux = nova.direita
        nova.direita = no
        no.esquerda = aux
        if(self.raiz == no):
            self.raiz = nova
            no.pai = nova
            nova.pai = None
        else:
            no.pai.esquerda = nova
            nova.pai = no.pai
            no.pai = nova
        self.atualizaBalanceamento(nova)
        self.atualizaBalanceamento(no)
    #def rotacaoEsquerdaDireita(self,no):
        #self.rotacaoEsquerda(no)
        #self.rotacaoDireita(no)
    #def rotacaoDireitaEsquerda(self,no):
        #self.rotacaoDireita(no)
        #self.rotacaoEsquerda(no)
    def balancear(self,no):
        if no.balanceamento < -1:
            aux = no.direita
            if(aux.direita):
                self.rotacaoEsquerda(no)
            else:
                print('rotação dupla:direita-esquerda')
                pass
        elif  no.balanceamento > 1:
            aux = no.esquerda
            if aux.esquerda:
                self.rotacaoDireita(no)
            else:
                print('rotação dupla:esquerda-direita')
                pass
        else:
            pass




    def atualizaBalanceamento(self,no):
        no.balanceamento = self.altura(no.esquerda) - self.altura(no.direita)
        if no.balanceamento > 1 or no.balanceamento < -1:
            self.balancear(no)
            return
        if no.pai != None:
            if no.pai.esquerda == no:
                no.pai.balanceamento +=1
            elif no.pai.direita == no:
                no.pai.balanceamento -=1
            if no.pai.balanceamento != 0:
                self.atualizaBalanceamento(no.pai)



