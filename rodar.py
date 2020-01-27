from jogo import Jogo
from jogador import Jogador

jogadores = ['Ana', 'Beto', 'Carlos']
jogo = Jogo()

for j in jogadores:
    jogo.adiciona_jogador(Jogador(j))

print('Jogo')
print(repr(jogo.jogadores))
print(repr(jogo.baralho))

jogo.novo_jogo()
