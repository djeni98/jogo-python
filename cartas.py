PAUS = 'p'
COPAS = 'c'
ESPADAS = 'e'
SALMORA = 's' # Também conhecido como Mole

NAIPE = (PAUS, COPAS, ESPADAS, SALMORA)

# Colocar os emojis para representar os naipes
ICONE_NAIPE = {
    PAUS: 'P',
    COPAS: 'C',
    ESPADAS: 'E',
    SALMORA: 'S'
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

class Carta(object):
    """Representa uma carta do baralho"""

    def __init__(self, naipe, valor, manilha=FALSE):
        self.naipe = naipe
        self.valor = valor
        self.manilha = manilha

    def __str__(self):
        return '%s_%s_%s' % (self.naipe, self.valor, self.manilha)

def from_str(string):
    """Transforma string em Carta"""
    naipe, valor, manilha = string.split('_')
    return Carta(naipe, valor, manilha)
        
