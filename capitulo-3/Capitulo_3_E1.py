
class Node():

    def __init__(self, posicoesAtual, estado=None, profundidade=None):
        self.PROFUNDIDADE_MAX = 5
        self.posicoesAtual = posicoesAtual
        if estado == None:
            self.estado = "Inicio"
        else:
            self.estado = estado
        if profundidade == None:
            self.profundidade = 0
        else:
            self.profundidade = profundidade
        self.childNodes = []
        self.imprimirPuzzle()
        self.iniciarArvore()

    def moverParaEsquerda(self):
        if self.posicaoZero() % 3 > 0 and self.profundidade < self.PROFUNDIDADE_MAX and self.estado != 'Direita':
            novo = self.posicoesAtual.copy()
            novo = self.trocarPos(novo, -1)
            self.childNodes.append(Node(novo, 'Esquerda', self.profundidade + 1))

    def moverParaDireita(self):
        if self.posicaoZero() % 3 < 2 and self.profundidade < self.PROFUNDIDADE_MAX and self.estado != 'Esquerda':
            novo = self.posicoesAtual.copy()
            novo = self.trocarPos(novo, 1)
            self.childNodes.append(Node(novo, 'Direita', self.profundidade + 1))

    def moverParaCima(self):
        if self.posicaoZero() - 3 >= 0 and self.profundidade < self.PROFUNDIDADE_MAX and self.estado != 'Baixo':
            novo = self.posicoesAtual.copy()
            novo = self.trocarPos(novo, -3)
            self.childNodes.append(Node(novo, 'Cima', self.profundidade + 1))

    def moverParaBaixo(self):
        if self.posicaoZero() + 3 < len(self.posicoesAtual) and self.profundidade < self.PROFUNDIDADE_MAX and self.estado != 'Cima':
            novo = self.posicoesAtual.copy()
            novo = self.trocarPos(novo, 3)
            self.childNodes.append(Node(novo, 'Baixo', self.profundidade + 1))

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
        print(f'{self.estado}\nProfundidade: {self.profundidade}')
        print(f'| {self.posicoesAtual[0]} {self.posicoesAtual[1]} {self.posicoesAtual[2]} |')
        print(f'| {self.posicoesAtual[3]} {self.posicoesAtual[4]} {self.posicoesAtual[5]} |')
        print(f'| {self.posicoesAtual[6]} {self.posicoesAtual[7]} {self.posicoesAtual[8]} |\n')

    def iniciarArvore(self):
        self.moverParaEsquerda()
        self.moverParaBaixo()
        self.moverParaDireita()
        self.moverParaCima()

    def verificar(self,novo):
        i = 0
        while i < len(self.antecessor):
            if novo[i] != self.antecessor[i]:
                return False
            i += 1
        return True

def executar():

    puzzle = Node([3, 1, 2, 6, 0, 5, 7, 4, 8])

if __name__ == "__main__":
    executar()