class No:
    
    def __init__(self, key, dir, esq):
        self.element = key
        self.dir = dir
        self.esq = esq

class Tree:

    def __init__(self):
        self.root = No(None,None,None)
        self.root = None

    #Função inserir
    def inserir(self, valor):
        novo = No(valor, None, None) #cria um novo Nó
        if self.root == None:
            self.root = novo
        else: #se não for a raiz
            atual = self.root
            while True:
                anterior = atual
                if valor <= atual.element:
                    atual = atual.esq
                    if atual == None:
                         anterior.esq = novo
                         return 
                #fim da condição para a esquerda
                else: #ir para a direita
                    atual = atual.dir
                    if atual == None:
                            anterior.dir = novo
                            return
                #fim da condição para a direita

    def raiz(self, atual):
         if atual != None:
              print(atual.element,end=" ")

    def mostrarRaiz(self):
          print("A raiz é: ",end="")
          self.raiz(self.root)

    #Função buscar
    def buscar(self, key):
        if self.root == None:
            return None #se arvore vazia
        atual = self.root #procura pela raiz
        while atual.element != key:
            if key < atual.element:
                atual = atual.esq
            else:
                atual = atual.dir
            if atual == None:
                return None
        return atual

    #função que define qual Nó será o sucessor do que foi removido
    def noSucessor(self, noApaga):
        paiSucessor = noApaga
        sucessor = noApaga
        atual = noApaga.dir  #vai para a subarvore a direita

        while atual != None: #enquanto não chegar no Nó mais a esquerda
            paiSucessor = sucessor
            sucessor = atual
            atual = atual.esq #vai para a esquerda
        #quando sair do while sucessor será o Nó mais a esquerda da subarvore a direita
        #paiSucessor será o pai de sucessor e apaga o Nó que deve ser eliminado

        if sucessor != noApaga.dir:
            paiSucessor.esq = sucessor.dir
            sucessor.dir = noApaga.dir
            #guarda a posição de referência a direita do sucessor
            #quando ele assumir a posição correta na arvore
        
        return sucessor
    #função remover

    def remover(self, valor):
        if self.root == None:
            return False
        atual = self.root
        pai = self.root
        filho_Es = True

        #busca ao valor
        while atual.element != valor:
            pai = atual
            if valor < atual.element:
                atual = atual.esq
                filho_Es = True
            else:
                atual = atual.dir
                filho_Es = False
            if atual == None:
                return False
        #fim da busca pelo valor

        if atual.esq == None and atual.dir == None:
             if atual == self.root:
                self.root = None #se for a raiz
            
             else:
                if filho_Es:
                     pai.esq = None #se for filho a esquerda do pai
                else:
                    pai.dir = None #se for filho a direita do pai

        # Se é pai e nao possui um filho a direita, substitui pela subarvore a direita
        elif atual.dir == None:
            if atual == self.root:
                self.root = atual.esq
            else:
                if filho_Es:
                    pai.esq = atual.dir
                else:
                    pai.dir = atual.dir
        
        # Se é pai e nao possui um filho a esquerda, substitui pela subarvore a esquerda
        elif atual.esq == None:
            if atual == self.root:
                self.root = atual.dir
            else:
                if filho_Es:
                    pai.esq = atual.dir
                else:
                    pai.dir = atual.dir

        
        else:
            sucessor = self.noSucessor(atual)

            if atual == self.root:
                self.root = sucessor
            else:
                if filho_Es:
                    pai.esq = sucessor
                else:
                    pai.dir = sucessor
            sucessor.esq = atual.esq

        return True


### Início da main ###    
arv = Tree()
print("Árvore Binária de Busca")

op = 0
while op != 5:
       print("\n")
       print("------------------------------------------")
       print("Inicie o programa")
       print("1--Inserir")
       print("2--Excluir")
       print("3--Pesquisar")
       print("4--Exibir raiz")
       print("5--Sair")
       print("------------------------------------------")

       op = int(input(": "))
       if op == 1:
           x = int(input("Informe o valor: "))
           arv.inserir(x)
       elif op == 2:
           x = int(input("Informe o valor: "))
           if arv.remover(x) == False:
                 print("Valor nao encontrado!")
       elif op == 3:
           x = int(input("Informe o valor: "))
           if arv.buscar(x) != None:
               print("Valor encontrado")

           else:
               print("Valor não encontrado")

       elif op == 4:
          arv.mostrarRaiz()

       elif op == 5:
           break