import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)

texto = 'Ola Mundo Pygame'

fonte = pygame.font.SysFont('arial', 48, True, False)

img_texto = fonte.render(texto, True, (255,255,0))

while True:
    screen.blit(img_texto,(100, 100))
    pygame.display.update()

    for acao in pygame.event.get():
        if acao.type == pygame.QUIT:
            exit()
