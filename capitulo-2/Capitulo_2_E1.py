import random as rd

class Ambiente():

    def __init__(self, salas):
        self.salas = salas

    def sujarSala(self):
        for i in range(self.tamanho()):
            if rd.randint(0, 1):
                self.salas[i] = 1


    def estaSujo(self, pos: int):

        return self.salas[pos] == 1

    def removerSujeira(self, i: int):
        self.salas[i] = 0

    def imprimirSalas(self):
        print(self.salas)

    def ehParede(self, pos):
        return pos >= self.tamanho() or pos < 0;

    def tamanho(self):
        return len(self.salas)

class Aspidador():

    def __init__(self, amb: Ambiente, pos: int):

        self.ambiente = amb

        self.posAspirador = pos

        self.pontuacao = 0

    def iniciarLimpeza(self, interacoes: int):
        i = 1
        direcao = 1
        # direcao == 1 -> direita
        # direcao == 0 -> esquerda

        while i <= interacoes:

            if self.ambiente.estaSujo(self.posAspirador):
                self.__limpar()
                self.__adicionarPontuacao()

            elif direcao:
                direcao = self.__moverDireita()
            else:
                direcao = self.__moverEsquerda()

            self.ambiente.sujarSala()
            i += 1

    def pontuacao(self):
        return self.pontuacao

    def __moverDireita(self):
        if self.ambiente.ehParede(self.posAspirador + 1): # NoOp
            return 0 # Muda de direcao
        else: # Direita
            self.posAspirador += 1
            return 1

    def __moverEsquerda(self):
        if self.ambiente.ehParede(self.posAspirador - 1): # NoOp
            return 1 # Muda de direcao
        else: # Esquerda
            self.posAspirador -= 1
            return 0

    def __limpar(self):
        self.ambiente.removerSujeira(self.posAspirador)

    def __adicionarPontuacao(self):
        self.pontuacao += 1

class main():

    # 0 == Limpo
    # 1 == Sujo

    salas1 = [[0, 0], [0, 1], [1, 0], [1, 1]]
    salas2 = [[0, 0], [0, 1], [1, 0], [1, 1]]

    amb1 = [Ambiente(salas1[0]), Ambiente(salas1[1]), Ambiente(salas1[2]), Ambiente(salas1[3])]
    amb2 = [Ambiente(salas2[0]), Ambiente(salas2[1]), Ambiente(salas2[2]), Ambiente(salas2[3])]

    agnt1 = [Aspidador(amb1[0], 0), Aspidador(amb1[1], 0), Aspidador(amb1[2], 0), Aspidador(amb1[3], 0),
             Aspidador(amb2[0], 1), Aspidador(amb2[1], 1), Aspidador(amb2[2], 1), Aspidador(amb2[3], 1)]

    i = 0
    val = 0
    soma = 0

    while i < len(agnt1):

        agnt1[i].iniciarLimpeza(1000)
        val = agnt1[i].pontuacao
        soma += val
        print(f'Caso {i + 1}: \nPontuação = {val}\n')
        i += 1

    print(f'Média total: {soma / len(agnt1) :.2f}')