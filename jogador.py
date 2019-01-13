class Jogador(object):
    def __init__(self, user):
        self.cartas = list()
        self.nome = user.first_name

    def inicia_vida(self, vidas):
        self.vidas = vidas

    def pega_mao(self, baralho):
        self.cartas = baralho.pega_cartas(self.vidas)

    def imprime_mao(self):
        mao = ""
        for carta in self.cartas:
            mao += str(carta) + " "
        texto = "As cartas de {0} são {1}".format(self.nome, mao)
        return texto
