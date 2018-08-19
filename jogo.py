from cartas import Baralho

# seleciona item da tupla
from random import choice

class Jogo(object):
    
    # ----- Pra que esse campo? ----- #
    # manilha = None
    
    def __init__(self, chat):
        self.chat = chat
        # guardar os jogadores que irão jogar
        self.baralho = Baralho()
     
    def nova_partida(self):
        # iniciar vida dos jogadores

    def nova_rodada(self):
        """Embaralha e entrega as cartas para os jogadores"""
        # escolha do vira
        vira_valor = choice(VALORES)
        vira_naipe = choice(NAIPES)

        self.baralho.novo_baralho(vira_valor, vira_naipe)

        # entregar as cartas para os jogadores
        # escolher a manilha
   
    def start(self):
        
