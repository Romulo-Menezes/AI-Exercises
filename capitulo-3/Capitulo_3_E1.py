
class Node():

    def __init__(self, posicoesAtual, estado=None, profundidade=None):
        self.posicoesAtual = posicoesAtual
        if estado == None:
            self.movimento = "Inicio"
        else:
            self.movimento = estado
        if profundidade == None:
            self.profundidade = 0
        else:
            self.profundidade = profundidade
        self.meta = self.verificarMeta()
        self.nosFilho = list()
        #self.imprimirPuzzle()


    def moverParaEsquerda(self):
        if self.posicaoZero() % 3 > 0 and self.movimento != 'Direita':
            novo = self.posicoesAtual.copy()
            novo = self.trocarPos(novo, -1)
            self.nosFilho.append(Node(novo, 'Esquerda', self.profundidade + 1))

    def moverParaDireita(self):
        if self.posicaoZero() % 3 < 2 and self.movimento != 'Esquerda':
            novo = self.posicoesAtual.copy()
            novo = self.trocarPos(novo, 1)
            self.nosFilho.append(Node(novo, 'Direita', self.profundidade + 1))

    def moverParaCima(self):
        if self.posicaoZero() - 3 >= 0 and self.movimento != 'Baixo':
            novo = self.posicoesAtual.copy()
            novo = self.trocarPos(novo, -3)
            self.nosFilho.append(Node(novo, 'Cima', self.profundidade + 1))

    def moverParaBaixo(self):
        if self.posicaoZero() + 3 < len(self.posicoesAtual) and self.movimento != 'Cima':
            novo = self.posicoesAtual.copy()
            novo = self.trocarPos(novo, 3)
            self.nosFilho.append(Node(novo, 'Baixo', self.profundidade + 1))

    def trocarPos(self, vetor, orientacao):
        posZero = self.posicaoZero()
        temp = vetor[posZero]
        vetor[posZero] = vetor[posZero + (orientacao)]
        vetor[posZero + (orientacao)] = temp
        return vetor

    def posicaoZero(self):
        i = 0
        while i < len(self.posicoesAtual):
            if self.posicoesAtual[i] == 0:
                break
            i += 1
        return i

    def imprimirPuzzle(self):
        print(f'{self.movimento}\nProfundidade: {self.profundidade}')
        print(f'| {self.posicoesAtual[0]} {self.posicoesAtual[1]} {self.posicoesAtual[2]} |')
        print(f'| {self.posicoesAtual[3]} {self.posicoesAtual[4]} {self.posicoesAtual[5]} |')
        print(f'| {self.posicoesAtual[6]} {self.posicoesAtual[7]} {self.posicoesAtual[8]} |\n')

    def gerarFilhos(self):
        if not self.meta:
            self.moverParaEsquerda()
            self.moverParaBaixo()
            self.moverParaDireita()
            self.moverParaCima()

    def verificarMeta(self):
        return self.posicoesAtual == [0,1,2,3,4,5,6,7,8]

    def __str__(self): # Vai ser utilizado para o dicionario
        return ''.join(str(val) for val in self.posicoesAtual) + self.movimento + str(self.profundidade)

def bfs(no):
    fronteira = [no]                                            # Fronteira da busca
    nosPai = dict()                                             # Dicionario para armazenar os nós pai dos nós filho
    visitados = [no]                                            # Armazena os nós já visitados
    res = []                                                    # Vai armazenar o caminho
    achou = False

    while not achou:                                            # Só para quando achar solução
        pai = fronteira[0]
        del fronteira[0]

        if pai.meta:                                            # Verifica se achou o estado final do puzzle
            node = pai                                          # node vai ser utilizado para reconstruir o caminho
            node.imprimirPuzzle()
            while node.posicoesAtual != no.posicoesAtual:       # Volta até o estado inicial
                res.append(node.movimento)                      # Armazena todos os movimentos
                node = nosPai[str(node)]                        # node recebe o nó pai
            res.reverse()                                       # Inverte para ficar na posição certa
            print(f'Solução: {res}')
            achou = True

        pai.gerarFilhos()                                       # Gera os nós filhos
        for filho in pai.nosFilho:                              # Para cada filho gerado, ira verificar se já foi
            if filho not in visitados:                          # visitado. Se não foi vai ser adicionado na lista
                visitados.append(filho)                         # e vai ser adicionado no dicionario o pai com base
                nosPai[str(filho)] = pai                        # no filho.
                fronteira.append(filho)                         # Adiciona o filho na fronteira


def executar():

    puzzle = Node([3, 1, 2, 6, 0, 5, 7, 4, 8])
    puzzle.imprimirPuzzle()
    bfs(puzzle)

if __name__ == "__main__":
    executar()