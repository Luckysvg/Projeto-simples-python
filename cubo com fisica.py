import pygame
import sys
import random

pygame.init()

# janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cubo evoluído")

clock = pygame.time.Clock()

# cubo
x = 350
y = 400
tamanho = 80

velocidade = 4

# física
vel_y = 0
gravidade = 0.5
no_chao = False

# cor
cor = (0, 200, 255)

# fonte
fonte = pygame.font.SysFont("Arial", 24)

while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # mudar cor com C
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_c:
                cor = (
                    random.randint(0,255),
                    random.randint(0,255),
                    random.randint(0,255)
                )

            # pular com espaço
            if evento.key == pygame.K_SPACE and no_chao:
                vel_y = -12

    teclas = pygame.key.get_pressed()

    # mover lados
    if teclas[pygame.K_LEFT]:
        x -= velocidade

    if teclas[pygame.K_RIGHT]:
        x += velocidade

    # gravidade
    vel_y += gravidade
    y += vel_y

    # chão
    if y >= altura - tamanho:
        y = altura - tamanho
        vel_y = 0
        no_chao = True
    else:
        no_chao = False

    # limites laterais
    if x < 0:
        x = 0

    if x > largura - tamanho:
        x = largura - tamanho

    # desenhar
    tela.fill((30, 30, 30))

    pygame.draw.rect(tela, cor, (x, y, tamanho, tamanho))

    # texto coordenadas
    texto = fonte.render(f"X: {x}  Y: {int(y)}", True, (255,255,255))
    tela.blit(texto, (10,10))

    texto2 = fonte.render("Setas = mover | ESPAÇO = pular | C = mudar cor", True, (255,255,255))
    tela.blit(texto2, (10,40))

    pygame.display.update()

    clock.tick(60)
