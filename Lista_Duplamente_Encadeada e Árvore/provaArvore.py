from provaListaDuplamente import Lista
class No():

    def __init__(self,elemento):
        self.elemento = elemento
        self.esquerda = None
        self.direita = None
        self.atualizaBalanceamento = 0
        self.pai = None
    def __str__(self):
        return str(self.elemento)

class Arvore():
    def __init__(self):
        self.raiz = None
        self.quanFolhas = 0

    def imprimirNo(self,elemento):
        if elemento != None:
            self.imprimirNo(elemento.esquerda)
            print(elemento, end = '-')
            self.imprimirNo(elemento.direita)
    def imprimir (self):
        return  self.imprimirNo(self.raiz)
#letra A da 2 questão
    def add(self,elemento):
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
                        no.atualizaBalanceamento =0
                        break
                elif no.elemento<perc.elemento:
                    if perc.esquerda != None:
                        perc = perc.esquerda
                    else:
                        perc.esquerda = no
                        no.atulizaBalanceamento = 0
                        break
                else:
                    raise Exception ('Elemento ja existe')
            self.quanFolhas += 1
    def rotacaoEsquerda(self,no):
        novo = no.direita
        aux = novo.esquerda
        novo.esquerda = no
        no.direita = aux
        if self.raiz == no:
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
        if self.raiz == no:
            self.raiz = nova
            no.pai = nova
            nova.pai = None
        else:
            no.pai.esquerda = nova
            nova.pai = no.pai
            no.pai = nova
        self.atualizaBalanceamento(nova)
        self.atualizaBalanceamento(no)
    def balancear(self,no):
        if no.balanceamento < -1:
            aux = no.direita
            if aux.direita:
                self.rotacaoEsquerda(no)
            else:
                print('rotação dupla:direita-esquerda')
                pass
        elif no.balanceamento > 1:
            aux = no.esquerda
            if aux.esquerda:
                self.rotacaoDireita(no)
            else:
                print('rotação dupla:esquerda-direita')
                pass
        else:
            pass
#letra B da 2ª questão
    def contarNos(self, perc):
        if perc == None:
            return 0
        else:
            return 1 + self.contarNos(perc.esquerda) + self.contarNos(perc.direita)
#letra C da 2ª questão
    def altura(self, perc):
        if perc == None or perc.esquerda== None and perc.direita == None:
            return 0
        else:
            alturaEsquerda = self.altura(perc.esquerda)
            alturaDireita = self.altura(perc.direita)
            return max(alturaEsquerda,alturaDireita) + 1
#letra D da 2ª questão
    def Listar(self):
        lista = Lista()
        def emOrdem(perc):
            if perc != None:
                emOrdem(perc.esquerda)
                lista.add_fim(perc.elemento)
                emOrdem(perc.direita)
        emOrdem(self.raiz)
        return lista
