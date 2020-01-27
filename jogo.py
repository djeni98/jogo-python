from cartas import Baralho, VALORES, NAIPES
from random import choice
# seleciona item da tupla

def getAposta(jogador):
    print(' --- Jogador {} ---'.format(jogador.nome))
    jogador.imprime_mao()
    print('Quantas faz {}?'.format(jogador.nome))
    ap = None
    while ap == None:
        try:
            ap = int(input())
            if ap < 0:
                ap = None
                print('Digite um número inteiro não negativo')
        except ValueError:
            ap = None
            print('Digite um número inteiro não negativo')

    return ap

class Jogo(object):
    def __init__(self):
        self.baralho = Baralho()
        self.jogadores = list()

    def __repr__(self):
        jogadores = '['
        for j in self.jogadores:
            jogadores += ' ' + j.nome
        jogadores += ' ]'
        return '<Jogo jogadores={}>'.format(jogadores)

    def adiciona_jogador(self, jogador):
        if len(self.jogadores) < 8:
            self.jogadores.append(jogador)
        else:
            print("Não foi possível adicionar")

    def manutencao_jogadores(self):
        jogadores = list()
        for jogador in self.jogadores:
            if jogador.vidas > 0:
                jogadores.append(jogador)

        if len(jogadores) == 1:
            return jogadores[0]
        else:
            self.jogadores = jogadores[1:]
            self.jogadores.append(jogadores[0])
            return None

    def nova_rodada(self, jogadores):
        return choice(jogadores).nome

    def nova_partida(self):
        vira_valor = choice(VALORES)
        vira_naipe = choice(NAIPES)
        self.baralho.novo_baralho(vira_valor, vira_naipe)

        rodadas = 0
        for jogador in self.jogadores:
            jogador.pega_mao(self.baralho)
            jogador.imprime_mao()
            rodadas = jogador.vidas if jogador.vidas > rodadas else rodadas

        # quantas faz
        print(self.baralho)
        aposta = { jogador.nome: getAposta(jogador) for jogador in self.jogadores}
        # Implementar soma das apostas != rodadas

        jogo = { jogador.nome: 0 for jogador in self.jogadores }

        for vida in range(rodadas):
            jogadores_ativos = list()
            for jogador in self.jogadores:
                if jogador.vidas > vida:
                    jogadores_ativos.append(jogador)

            quem_fez = self.nova_rodada(jogadores_ativos)
            print('rodada {}, vencedor {}'.format(vida, quem_fez))

            jogo[quem_fez] += 1

        for jogador in self.jogadores:
            jogador.vidas -= abs(aposta[jogador.nome] - jogo[jogador.nome])

        return self.manutencao_jogadores()

    def novo_jogo(self):
        if len(self.jogadores) < 2:
            print("Jogadores mínimos não atingido")
            return

        for jogador in self.jogadores:
            jogador.inicia_vida(5)

        #self.nova_partida()
        vencedor = None
        while not vencedor:
            vencedor = self.nova_partida()
            # Rotaciona jogadores
            # Retira com vida = 0
        print("Vencedor: " + vencedor.nome)

