class Jogador(object):
    def __init__(self, nome):
        self.cartas = list()
        self.nome = nome
        self.vidas = None

    def __repr__(self):
        if self.vidas == None:
            return '<Jogador nome={}>'.format(self.nome)
        return '<Jogador nome={}, vidas={}>'.format(self.nome, self.vidas)

    def inicia_vida(self, vidas):
        self.vidas = vidas

    def pega_mao(self, baralho):
        self.cartas = baralho.pega_cartas(self.vidas)

    def joga_carta(self, indice):
        return self.cartas.pop(indice)

    def imprime_mao(self):
        mao = ""
        for carta in self.cartas:
            mao += str(carta) + " "
        texto = "As cartas de {0} são {1}".format(self.nome, mao)
        print(texto)
        return texto

    def imprime_cartas(self):
        mao = " > "
        indices = " > "
        for i, carta in enumerate(self.cartas):
            mao += str(carta) + " "
            indices += " " + str(i) + " "

        print(mao)
        print(indices)
