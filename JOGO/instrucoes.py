import pygame
from pygame import *
from animacoes import *

def instrucoes():
    pygame.init()
    tela = pygame.display.set_mode([900, 400])
    pygame.display.set_caption("SPACE INVADERS")
    pygame.font.init()

    background_name = 'imagens/background_title.png'
    background = pygame.image.load(background_name).convert()
    y_bg = 0

    fonte_cosmic ='fonte/cosmic.ttf'
    titlefont = pygame.font.Font(fonte_cosmic, 55)
    textfont = pygame.font.Font(fonte_cosmic, 20)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)

    Sair = False
    while Sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    Sair = True
                    break

        tela.fill(BLACK)
        tela.blit(background, (0, y_bg))
        title = titlefont.render("INSTRUCOES PARA NOOBS", True, YELLOW)
        title_shade = titlefont.render("INSTRUCOES PARA NOOBS", True, WHITE)
        text = textfont.render("> Mover-se para os lados = Setas direcionais", True, WHITE)
        text_shade = textfont.render("> Mover-se para os lados = Setas direcionais", True, BLUE)
        text1 = textfont.render("> Atirar = Espaco", True, WHITE)
        text1_shade = textfont.render("> Atirar = Espaco", True, BLUE)
        text2 = textfont.render("> Se voce for muito ruim, aperte Alt + F4 ;)", True, WHITE)
        text2_shade = textfont.render("> Se voce for muito ruim, aperte Alt + F4 ;)", True, BLUE)
        text_sair = textfont.render("Pressione Backspace para voltar ao menu", True, WHITE)

        tela.blit(title_shade, (18, 8))
        tela.blit(title, (20, 10))
        tela.blit(text_shade, (148, 98))
        tela.blit(text, (150, 100))
        tela.blit(text1_shade, (148, 148))
        tela.blit(text1, (150, 150))
        tela.blit(text2_shade, (148, 198))
        tela.blit(text2, (150, 200))
        tela.blit(text_sair, (310, 380))

        y_bg -= 0.05
        pygame.display.update()