import random as rd

class Ambiente():

    def __init__(self, salas):
        self.salas = salas

    def sujarSala(self):
        for i in range(self.tamanho()):
            if rd.randint(1, 10) > 6:
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

class Aspirador_1():

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

class Aspirador_2():

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

def __executar():

    i = soma = 0
    cont = 1
    status = ['Limpo', 'Sujo']
    rd.seed(7)

    while i < 2:
        j = 0
        sala = [[0, 0], [0, 1], [1, 0], [1, 1]]
        while j < 4:
            amb = Ambiente(sala[j])
            agnt = Aspirador_1(amb, i)

            print(f'Caso {cont}:\nSala: [{status[sala[j][0]]} , {status[sala[j][1]]}]\nPosição inicial do agente: {i}')

            agnt.iniciarLimpeza(1000)
            val = agnt.pontuacao
            soma += val
            print(f'Pontuação = {val}\n')

            j += 1
            cont += 1
        i += 1

    print(f'Média total do agente 1: {soma / 8 :.2f}\n\n{"-="*15}-\n')

    i = soma = 0
    cont = 1

    while i < 2:
        j = 0
        sala = [[0, 0], [0, 1], [1, 0], [1, 1]]
        while j < 4:
            amb = Ambiente(sala[j])
            agnt = Aspirador_2(amb, i)

            print(f'Caso {cont}:\nSala: [{status[sala[j][0]]} , {status[sala[j][1]]}]\nPosição inicial do agente: {i}')

            agnt.iniciarLimpeza(1000)
            val = agnt.pontuacao
            soma += val
            print(f'Pontuação = {val}\n')

            j += 1
            cont += 1
        i += 1

    print(f'Média total do agente 2: {soma / 8 :.2f}')

if __name__ == '__main__':
    __executar()
