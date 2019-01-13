from cartas import Baralho, VALORES, NAIPES
from random import choice
# seleciona item da tupla

class Jogo(object):
    def __init__(self, chat):
        self.chat = chat
        self.baralho = Baralho()
        self.jogadores = list()

    def adiciona_jogador(self, jogador):
        if len(self.jogadores) < 8:
            self.jogadores.append(jogador)
        else:
            print("Não foi possível adicionar")

    def nova_partida(self):
        """Embaralha e entrega as cartas para os jogadores"""
        vira_valor = choice(VALORES)
        vira_naipe = choice(NAIPES)
        self.baralho.novo_baralho(vira_valor, vira_naipe)

        rodadas = 0
        for jogador in self.jogadores:
            jogador.pega_mao(self.baralho)
            rodadas = jogador.vidas if jogador.vidas > rodadas else rodadas

        # quantas faz cada jogador?

        for vida in range(rodadas):
            jogadores_ativos = list()
            for jogador in self.jogadores:
                if jogador.vidas > vida:
                    jogadores_ativos.append(jogador)

            self.nova_rodada(jogadores_ativos)

    def nova_rodada(self, jogadores):

    def novo_jogo(self):
        if len(self.jogadores) < 2:
            print("Jogadores mínimos não atingido")
            return

        for jogador in self.jogadores:
            jogador.inicia_vida(5)

        vencedor = None
        while not vencedor:
            vencedor = self.nova_partida()


