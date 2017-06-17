
import pygame
from animacoes import *
from cronometro import *
from space_invaders import *
from instrucoes import *

def menu():
    pygame.init()
    tela = pygame.display.set_mode([900, 400])
    pygame.display.set_caption("SPACE INVADERS: Attack on Aliens Edition")
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

    #musica
    music = 'audios/menu_theme.ogg'
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)

    #cores
    cor_branco = (255, 255, 255)
    cor_preto = (0, 0, 0)
    cor_amarela = (255, 255, 000)
    sair = False

    #while para funcoes

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] >= 475 and mouse[1] >= 300:
                    if mouse[0] <= 595 and mouse[1] <= 320:
                        creditos()
                        pygame.mixer.music.load(music)
                        pygame.mixer.music.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] >= 620 and mouse[1] >= 300:
                    if mouse[0] <= 680 and mouse[1] <= 320:
                        sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] >= 210 and mouse[1] >= 300:
                    if mouse[0] <= 285 and mouse[1] <= 320:
                        jogo()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] >= 310 and mouse[1] >= 300:
                    if mouse[0] <= 430 and mouse[1] <= 320:
                        instrucoes()

    #adicionando fontes

        tela.fill(cor_preto)
        tela.blit(background, (0, y_bg))
        text = fonte_invaders.render('SPACE ', 1, (cor_amarela))
        text2 = fonte_invaders.render('INVADERS' ,1, (cor_amarela))
        text_shade = fonte_invaders.render('SPACE ', 1, (cor_branco))
        text2_shade= fonte_invaders.render('INVADERS' ,1, (cor_branco))
        edtitle = fonte_play.render('Attack on Alien Edition', 1, (cor_amarela))
        text3 = fonte_play.render('Jogar', 1, (cor_amarela))
        text4 = fonte_intrucao.render('Instrucoes', 1, (cor_amarela))
        text5 = fonte_credito.render('Creditos', 1, (cor_amarela))
        text6 = fonte_quit.render('Sair', 1, (cor_amarela))

        tela.blit(text_shade, (348, 98))
        tela.blit(text, (350, 100))
        tela.blit(text2_shade, (288, 158))
        tela.blit(text2,(290, 160))
        tela.blit(edtitle, (278, 210))
        tela.blit(text3,(210, 300))
        tela.blit(text4,(310, 300))
        tela.blit(text5,(475, 300))
        tela.blit(text6,(620, 300))
        y_bg -= 0.15
    #variavel para pegar a posicao do cursor
        mouse = pygame.mouse.get_pos()

    #variavel para atualizar o display
        pygame.display.update()
    pygame.quit()