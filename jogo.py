
from cartas import Baralho

class Jogo(object):
    
    manilha = None
    
    def __init__(self, chat):
        self.chat = chat
        # inicializar vidas dos jogadores
        self.baralho = Baralho()
     
    def nova_partida(self):
        """Embaralha e entrega as cartas para os jogadores"""
        self.baralho.novo_baralho()
        # entregar as cartas para os jogadores
        # escolher a manilha
   
    def start(self):
        
