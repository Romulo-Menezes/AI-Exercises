from collections import deque
import timeit
import resource

class Node():
    def __init__(self, tabela, noPai, movimento, profundidade):
        self.tabela = tabela
        self.movimento = movimento
        self.profundidade = profundidade
        self.pai = noPai
        self.nosFilho = list()
        self.ehMeta = self.__verificarMeta()
        self.map = self.__map()
        self.custo = h1(self.tabela) + self.profundidade

    def imprimirPuzzle(self):
        #print(f'Movimento: {self.movimento}\nProfundidade: {self.profundidade}')
        print(f'| {self.tabela[0]} {self.tabela[1]} {self.tabela[2]} |')
        print(f'| {self.tabela[3]} {self.tabela[4]} {self.tabela[5]} |')
        print(f'| {self.tabela[6]} {self.tabela[7]} {self.tabela[8]} |\n')

    def gerarFilhos(self):
        posZero = self.__posicaoZero()

        if posZero - 3 >= 0 and self.movimento != 'Cima':
            novaTabela = self.tabela.copy()
            novaTabela[posZero], novaTabela[posZero - 3] = novaTabela[posZero - 3], novaTabela[posZero]
            self.nosFilho.append(Node(novaTabela, self, 'Baixo', self.profundidade + 1))

        if posZero + 3 < len(self.tabela) and self.movimento != 'Baixo':
            novaTabela = self.tabela.copy()
            novaTabela[posZero], novaTabela[posZero + 3] = novaTabela[posZero + 3], novaTabela[posZero]
            self.nosFilho.append(Node(novaTabela, self, 'Cima', self.profundidade + 1))

        if posZero % 3 > 0 and self.movimento != 'Esquerda':
            novaTabela = self.tabela.copy()
            novaTabela[posZero], novaTabela[posZero - 1] = novaTabela[posZero - 1], novaTabela[posZero]
            self.nosFilho.append(Node(novaTabela, self, 'Direita', self.profundidade + 1))

        if posZero % 3 < 2 and self.movimento != 'Direita':
            novaTabela = self.tabela.copy()
            novaTabela[posZero], novaTabela[posZero + 1] = novaTabela[posZero + 1], novaTabela[posZero]
            self.nosFilho.append(Node(novaTabela, self, 'Esquerda', self.profundidade + 1))

    def menoresCusto(self):
        result = list()
        aux = 100000

        for filho in self.nosFilho:
            if filho.custo < aux:
                aux = filho.custo

        for filho in self.nosFilho:
            if filho.custo == aux:
                result.append(filho)

        return result

    def getCusto(self):
        return self.custo
    def __posicaoZero(self):
        i = 0
        while i < len(self.tabela):
            if self.tabela[i] == 0:
                break
            i += 1
        return i

    def __verificarMeta(self):
        return self.tabela == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __map(self):
        return ''.join(str(val) for val in self.tabela)


def bfs(noInicial):
    visitados, fronteira = set(), deque([noInicial])
    max_front, max_prof = 0, 0
    while fronteira:
        noAtual = fronteira.popleft()
        visitados.add(noAtual.map)

        if noAtual.ehMeta:
            return [noAtual, len(fronteira), max_front, len(visitados), max_prof]

        noAtual.gerarFilhos()
        for vizinhoAtual in noAtual.nosFilho:
            if vizinhoAtual.map not in visitados:
                fronteira.append(vizinhoAtual)
                visitados.add(vizinhoAtual.map)
            if max_prof < vizinhoAtual.profundidade:
                max_prof = vizinhoAtual.profundidade

        if len(fronteira) > max_front:
            max_front = len(fronteira)

def dfs(noInicial):
    visitados, fronteira = set(), deque([noInicial])
    max_front, max_prof = 0, 0

    while fronteira:
        noAtual = fronteira.pop()
        visitados.add(noAtual.map)

        if noAtual.ehMeta:
            return [noAtual, len(fronteira), max_front, len(visitados), max_prof]

        noAtual.gerarFilhos()
        for vizinhoAtual in reversed(noAtual.nosFilho):
            if vizinhoAtual.map not in visitados:
                fronteira.append(vizinhoAtual)
                visitados.add(vizinhoAtual.map)
            if max_prof < vizinhoAtual.profundidade:
                max_prof = vizinhoAtual.profundidade

        if len(fronteira) > max_front:
            max_front = len(fronteira)

def idfs(noInicial):
     max_alt = 1
     while True:
        visitados, fronteira = set(), deque([noInicial])
        max_front, max_prof = 0, 0
        while fronteira:
            noAtual = fronteira.pop()
            visitados.add(noAtual.map)

            if noAtual.ehMeta:
                return [noAtual, len(fronteira), max_front, len(visitados), max_prof]

            noAtual.gerarFilhos()
            for vizinhoAtual in reversed(noAtual.nosFilho):
                if vizinhoAtual.map not in visitados:
                    if vizinhoAtual.profundidade <= max_alt:
                        fronteira.append(vizinhoAtual)
                        visitados.add(vizinhoAtual.map)
                    if max_prof < vizinhoAtual.profundidade:
                        max_prof = vizinhoAtual.profundidade

            if len(fronteira) > max_front:
                max_front = len(fronteira)

        max_alt += 1

def ast(noInicial):
    visitados, fronteira = set(), [noInicial]
    max_front = 0
    max_prof = 0
    while fronteira:
        noAtual = fronteira.pop(0)
        visitados.add(noAtual.map)

        if noAtual.ehMeta:
            return [noAtual, len(fronteira), max_front, len(visitados), max_prof]

        noAtual.gerarFilhos()
        for vizinhoAtual in noAtual.nosFilho:
            if vizinhoAtual.map not in visitados:
                visitados.add(vizinhoAtual.map)
                fronteira.append(vizinhoAtual)
            if max_prof < vizinhoAtual.profundidade:
                max_prof = vizinhoAtual.profundidade

        fronteira = sorted(fronteira, key=Node.getCusto)

        if len(fronteira) > max_front:
            max_front = len(fronteira)

def bgu(noInicial):
    visitados, fronteira = set(), deque([noInicial])
    max_front, max_prof = 0, 0
    while fronteira:
        noAtual = fronteira.popleft()
        visitados.add(noAtual.map)

        if noAtual.ehMeta:
            return [noAtual, len(fronteira), max_front, len(visitados), max_prof]

        noAtual.gerarFilhos()
        for vizinhoAtual in noAtual.nosFilho:
            if vizinhoAtual.map not in visitados:
                visitados.add(vizinhoAtual.map)

            if max_prof < vizinhoAtual.profundidade:
                max_prof = vizinhoAtual.profundidade

        fronteira.append(noAtual.menoresCusto().copy().pop())

        if len(fronteira) > max_front:
            max_front = len(fronteira)


def obterCaminho(noFinal, noInicial):
    sol = []
    while noFinal.tabela != noInicial.tabela:
        sol.append(noFinal.movimento)
        #noFinal.imprimirPuzzle()
        noFinal = noFinal.pai
    sol.reverse()
    print('Caminho:', end=' ')
    print(sol)

def h1(tabela):
    somatorio = 0
    for i in range(0, 9):
        somatorio = somatorio + abs((i % 3) - (tabela[i] % 3)) + abs((i//3 - tabela[i]//3))
    return somatorio

def h2(tabela):
    somatorio = 0
    for i in range(0, 9):
        if i != tabela[i]:
            somatorio = somatorio + 2
    return somatorio

def executar():

    print('Insira a tabela e o método de busca da seguinte forma: bfs x,x,x,x,x,x,x,x,x')
    entrada = input()

    metodo = entrada.split(' ')[0]
    dados = entrada.split(' ')[1].split(',')
    tabela = []
    result = None
    tudoCerto = True
    for val in dados:
        tabela.append(int(val))

    puzzle = Node(tabela, None, None, 0)
    print('Entrada:')
    puzzle.imprimirPuzzle()

    comeco = timeit.default_timer()

    if metodo == 'bfs':
        result = bfs(puzzle)
    elif metodo == 'dfs':
        result = dfs(puzzle)
    elif metodo == 'idfs':
        result = idfs(puzzle)
    elif metodo == 'ast':
        result = ast(puzzle)
    elif metodo == 'bgu':
        result = bgu(puzzle)
    else:
        print('Método Inválido')
        tudoCerto = False

    fim = timeit.default_timer() - comeco

    if tudoCerto:
        print('Saida:')
        result[0].imprimirPuzzle()
        obterCaminho(result[0], puzzle)
        print(f'Custo do caminho: {result[0].profundidade}\n'
              f'Nós visitados: {result[3]}\n'
              f'Tamanho da fronteira: {result[1]}\n'
              f'Tamanho máximo da fronteira: {result[2]}\n'
              f'Profundidade da pesquisa: {result[0].profundidade}\n'
              f'Profundidade da pesquisa máxima: {result[4]}\n'
              f'Tempo de execução: {fim:.5f}\n'
              f'Máxima memória ram usada: {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000.0}')

if __name__ == "__main__":
    executar()