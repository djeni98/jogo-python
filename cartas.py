from random import shuffle

PAUS = 'p'
COPAS = 'c'
ESPADAS = 'e'
SALMORA = 's' # Também conhecido como Mole

NAIPES = (PAUS, COPAS, ESPADAS, SALMORA)

ICONE_NAIPES = {
    PAUS:    '♣',
    COPAS:   '♥',
    ESPADAS: '♠',
    SALMORA: '♦'
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
PESO_MANILHA = { SALMORA: 2, ESPADAS: 3, COPAS: 4, PAUS: 5 }

# Colocar os stickers
# STICKERS = { p_A: ____, p_2: ____ ..., s_K: ____ }

class Carta(object):
    """Representa uma carta do baralho"""

    # Manilha selecionada pelo 'Jogo'
    def __init__(self, valor, naipe, manilha):
        self.valor = valor
        self.naipe = naipe
        if valor == manilha:
            self.peso = PESO_MANILHA[naipe] * 100
        else:
            self.peso = PESO_COMUM[valor]*5 + PESO_MANILHA[naipe]

    def __eq__(self, x):
        return self.peso == x.peso

    def __lt__(self, x):
        return self.peso < x.peso

    def __str__(self):
        return "{0}{1}".format(self.valor, ICONE_NAIPES[self.naipe])

    def __repr__(self):
        return "<Carta {0}{1}>".format(self.valor, ICONE_NAIPES[self.naipe])

class Baralho(object):
    """Representa o baralho do jogo"""

    def __init__(self):
        self.cartas = list()
        self.vira = None

    def __repr__(self):
        return '<Baralho #cartas={}, vira={}>'.format(len(self.cartas), self.vira)

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
                    self.vira = Carta(valor, naipe, manilha_v)
                else:
                    self.cartas.append(Carta(valor, naipe, manilha_v))
        self.embaralha()

    def pega_cartas(self, qtde):
        mao = list()
        for i in range(qtde):
            if self.cartas:
                mao.append(self.cartas.pop())
            elif self.vira:
                mao.append(self.vira)
                # self.vira = None
        return mao

