import pygame

from constantes import AMARELO, PRETO

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)


class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 150
        self.raio = self.tamanho // 2

    def pintar(self, tela):
        # Desenha o corpo do Pacman
        pygame.draw.circle(
            tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0
        )

        # Desenho da boca do Pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]

        pygame.draw.polygon(tela, PRETO, pontos, 0)

        # Olho do Pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)

        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)


if __name__ == '__main__':

    pacman = Pacman()

    while True:
        # Pintar a tela
        pacman.pintar(screen)
        pygame.display.update()

        for acao in pygame.event.get():
            if acao.type == pygame.QUIT:
                exit()
