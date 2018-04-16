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

VALORES = (AS, DOIS, TRES, QUATRO, CINCO, SEIS, SETE, DAMA, VALETE, REI)

# Colocar os stickers
# STICKERS = { p_A: ____, p_2: ____ ..., s_K: ____ }

# Definir TRUE e FALSE para a manilha
TRUE = t
FALSE = f

class Carta(object):
    """Representa uma carta do baralho"""

    def __init__(self, valor, naipe, manilha=FALSE):
        self.valor = valor
        self.naipe = naipe
        self.manilha = manilha

    def __str__(self):
        return '%s_%s_%s' % (self.valor, self.naipe, self.manilha)

    def __repr__(self):
        return '%s%s' % (self.valor, ICONE_NAIPES[self.naipe])

def from_str(string):
    """Transforma string em Carta"""
    valor, naipe, manilha = string.split('_')
    return Carta(valor, naipe, manilha)

class Baralho(object):
    """Representa o baralho do jogo"""

    def __init__(self):
        self.cartas = list()

    def embaralha(self):
        """Embaralha"""
        shuffle(self.cartas)

    def novo_baralho(self):
        self.cartas.clear()
        for valor in VALORES:
            for naipe in NAIPES:
                self.cartas.append(Carta(valor, naipe))
        self.embaralha()


