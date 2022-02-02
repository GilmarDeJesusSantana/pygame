import pygame

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 1
RAIO = 30
pygame.init()
CORDENADA_X = 10
CORDENADA_Y = 10
VELOCIDADE_X = VELOCIDADE
VELOCIDADE_Y = VELOCIDADE

tela = pygame.display.set_mode((640, 480), 0)

while True:
    # Calcula as regras
    CORDENADA_X += VELOCIDADE_X
    CORDENADA_Y += VELOCIDADE_Y

    if CORDENADA_X + RAIO > 640:
        VELOCIDADE_X = -VELOCIDADE
    if CORDENADA_X - RAIO < 0:
        VELOCIDADE_X = VELOCIDADE

    if CORDENADA_Y + RAIO > 480:
        VELOCIDADE_Y = -VELOCIDADE
    if CORDENADA_Y - RAIO < 0:
        VELOCIDADE_Y = VELOCIDADE

    # Pinta
    tela.fill(PRETO)
    pygame.draw.circle(
        tela, AMARELO, (int(CORDENADA_X), int(CORDENADA_Y)), RAIO, 0
    )
    pygame.display.update()

    # Eventos
    for acao in pygame.event.get():
        if acao.type == pygame.QUIT:
            exit()
