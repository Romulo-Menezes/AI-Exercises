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

class Aspidador_1():

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
            self.__removerPontuacao()
            return 1

    def __moverEsquerda(self):
        if self.ambiente.ehParede(self.posAspirador - 1): # NoOp
            return 1 # Muda de direcao
        else: # Esquerda
            self.posAspirador -= 1
            self.__removerPontuacao()
            return 0

    def __limpar(self):
        self.ambiente.removerSujeira(self.posAspirador)

    def __adicionarPontuacao(self):
        self.pontuacao += 1

    def __removerPontuacao(self):
        self.pontuacao -= 1

class Aspidador_2():

    def __init__(self, amb: Ambiente, pos: int):

        self.ambiente = amb

        self.posAspirador = pos

        self.pontuacao = 0

    def iniciarLimpeza(self, interacoes: int):
        i = 1

        while i <= interacoes:

            if self.ambiente.estaSujo(self.posAspirador):
                self.__limpar()
                self.__adicionarPontuacao()
            else:
                self.__verificarSalasDoLado()

            self.ambiente.sujarSala()
            i += 1

    def pontuacao(self):
        return self.pontuacao

    def __verificarSalasDoLado(self):

        if self.ambiente.ehParede(self.posAspirador + 1) == 0 and self.ambiente.estaSujo(self.posAspirador + 1):
            self.__moverDireita()
        elif self.ambiente.ehParede(self.posAspirador - 1) == 0 and self.ambiente.estaSujo(self.posAspirador - 1):
            self.__moverEsquerda()


    def __moverDireita(self):
        self.posAspirador += 1
        self.__removerPontuacao()


    def __moverEsquerda(self):
        self.posAspirador -= 1
        self.__removerPontuacao()

    def __limpar(self):
        self.ambiente.removerSujeira(self.posAspirador)

    def __adicionarPontuacao(self):
        self.pontuacao += 1

    def __removerPontuacao(self):
        self.pontuacao -= 1

class main():

    # 0 == Limpo
    # 1 == Sujo

    salas1 = [[0, 0], [0, 1], [1, 0], [1, 1]]
    salas2 = [[0, 0], [0, 1], [1, 0], [1, 1]]

    salas3 = [[0, 0], [0, 1], [1, 0], [1, 1]]
    salas4 = [[0, 0], [0, 1], [1, 0], [1, 1]]

    amb1 = [Ambiente(salas1[0]), Ambiente(salas1[1]), Ambiente(salas1[2]), Ambiente(salas1[3])]
    amb2 = [Ambiente(salas2[0]), Ambiente(salas2[1]), Ambiente(salas2[2]), Ambiente(salas2[3])]

    amb3 = [Ambiente(salas3[0]), Ambiente(salas3[1]), Ambiente(salas3[2]), Ambiente(salas3[3])]
    amb4 = [Ambiente(salas4[0]), Ambiente(salas4[1]), Ambiente(salas4[2]), Ambiente(salas4[3])]

    agnt1 = [Aspidador_1(amb1[0], 0), Aspidador_1(amb1[1], 0), Aspidador_1(amb1[2], 0), Aspidador_1(amb1[3], 0),
             Aspidador_1(amb2[0], 1), Aspidador_1(amb2[1], 1), Aspidador_1(amb2[2], 1), Aspidador_1(amb2[3], 1)]

    agnt2 = [Aspidador_2(amb3[0], 0), Aspidador_2(amb3[1], 0), Aspidador_2(amb3[2], 0), Aspidador_2(amb3[3], 0),
            Aspidador_2(amb4[0], 1), Aspidador_2(amb4[1], 1), Aspidador_2(amb4[2], 1), Aspidador_2(amb4[3], 1)]

    i = 0
    val = 0
    soma = 0

    while i < len(agnt1):

        agnt1[i].iniciarLimpeza(1000)
        val = agnt1[i].pontuacao
        soma += val
        print(f'Caso {i + 1}: \nPontuação = {val}\n')
        i += 1

    print(f'Média total do agente 1: {soma / len(agnt1) :.2f}')

    i = 0
    soma = 0
    while i < len(agnt2):

        agnt2[i].iniciarLimpeza(1000)
        val = agnt2[i].pontuacao
        soma += val
        print(f'Caso {i + 1}: \nPontuação = {val}\n')
        i += 1

    print(f'Média total do agente 2: {soma / len(agnt2) :.2f}')