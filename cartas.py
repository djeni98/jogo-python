from random import shuffle

PAUS = 'p'
COPAS = 'c'
ESPADAS = 'e'
SALMORA = 's' # Também conhecido como Mole

NAIPES = (PAUS, COPAS, ESPADAS, SALMORA)

# Colocar os emojis para representar os naipes
ICONE_NAIPES = {
    PAUS: '♧',
    COPAS: '♡',
    ESPADAS: '♤',
    SALMORA: '♢'
}

AS = 'A'
DOIS = '2'
TRES = '3'
QUATRO = '4'
CINCO = '5'
SEIS = '6'
SETE = '7'
DAMA = 'Q'
VALETE = 'J'
REI = 'K'

VALORES = (QUATRO, CINCO, SEIS, SETE, DAMA, VALETE, REI, AS, DOIS, TRES)
PESO_COMUM = { valor: peso for peso, valor in enumerate(VALORES) }
PESO_MANILHA = { SALMORA: 11, ESPADAS: 12, COPAS: 13, PAUS: 14 }

# Colocar os stickers
# STICKERS = { p_A: ____, p_2: ____ ..., s_K: ____ }

# Definir TRUE e FALSE para a manilha
# TRUE = t
# FALSE = f

class Carta(object):
    """Representa uma carta do baralho"""

    # Manilha selecionada pelo 'Jogo'
    def __init__(self, valor, naipe, manilha):
        self.valor = valor
        self.naipe = naipe
        self.peso = PESO_MANILHA[naipe] if valor == manilha else PESO_COMUM[valor]

    def __eq__(self, x):
        return self.peso == x.peso

    def __lt__(self, x):
        return self.peso < x.peso

# ----- Pra que esta função? ----- #
# Manilha selecionada pelo 'Jogo'
#def from_str(string, manilha):
#    """Transforma string em Carta"""
#    valor, naipe = string.split('_')
#    return Carta(valor, naipe, manilha)
# -------------------------------- #

class Baralho(object):
    """Representa o baralho do jogo"""

    def __init__(self):
        self.cartas = list()

    def embaralha(self):
        """Embaralha"""
        shuffle(self.cartas)

    # Manilha selecionada pelo 'Jogo'
    def novo_baralho(self, vira_v, vira_n):
        self.cartas.clear()
        manilha_v = QUATRO if vira_v == TRES else VALORES[VALORES.index(vira_v)+1] 
        for valor in VALORES:
            for naipe in NAIPES:
                if(valor == vira_v and naipe == vira_n):
                    continue
                self.cartas.append(Carta(valor, naipe, manilha_v))
        self.embaralha()


