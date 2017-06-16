import pygame
from animacoes import *
from cronometro import *


def menu():
    pygame.init()
    tela = pygame.display.set_mode([900, 400])
    pygame.display.set_caption("SPACE INVADERS")
    pygame.font.init()

    # BackGround
    background_name = 'imagens/background_title.png'
    background = pygame.image.load(background_name).convert()
    y_bg = 0
    #fontes

    fonte_name = 'fonte/cosmic.ttf'
    fonte_space = pygame.font.SysFont(fonte_name, 55)
    fonte_invaders = pygame.font.Font(fonte_name, 55)
    fonte_play = pygame.font.Font(fonte_name, 20)
    fonte_intrucao = pygame.font.Font(fonte_name, 20)
    fonte_credito = pygame.font.Font(fonte_name, 20)
    fonte_quit = pygame.font.Font(fonte_name, 20)



    #cores

    cor_branco = (255, 255, 255)
    cor_preto = (0, 0, 0)
    cor_amarela = (255, 255, 000)
    sair = False

    #while para sair ao ser pressionado o botão X no canto da tela

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True


    #adicionando fontes

        tela.fill(cor_preto)
        tela.blit(background, (0, y_bg))
        text = fonte_invaders.render('SPACE ', 1, (cor_amarela))
        text2 = fonte_invaders.render('INVADERS' ,1, (cor_amarela))
        text3 = fonte_play.render('Jogar', 1, (cor_amarela))
        text4 = fonte_intrucao.render('Instrucoes', 1, (cor_amarela))
        text5 = fonte_credito.render('Creditos', 1, (cor_amarela))
        text6 = fonte_quit.render('Sair', 1, (cor_amarela))
        tela.blit(text, (350, 100))
        tela.blit(text2,(290, 160))
        tela.blit(text3,(210, 300))
        tela.blit(text4,(310, 300))
        tela.blit(text5,(475, 300))
        tela.blit(text6,(620, 300))
        y_bg -= 0.05

        if y_bg < -1600:
            introduçao()
            y_bg = 0

        pygame.display.update()


    pygame.quit()


