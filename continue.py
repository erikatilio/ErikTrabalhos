from cronometro import *


def continuar():
    import pygame

    pygame.init()
    tela = pygame.display.set_mode([900, 400])
    pygame.display.set_caption("SPACE INVADERS")
    pygame.font.init()

    # fontes

    fonte_name = 'fonte/cosmic.ttf'
    fonte_space = pygame.font.SysFont(fonte_name, 55)
    fonte_invaders = pygame.font.Font(fonte_name, 55)

    # cores

    cor_branco = (255, 255, 255)
    cor_preto = (0, 0, 0)
    cor_amarela = (255, 255, 000)
    sair = False
    x = '10'
    # while para sair ao ser pressionado o botão X no canto da tela

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

        # adicionando fontes

        tela.fill(cor_preto)

        text = fonte_invaders.render(x, 1, (cor_amarela))
        text2 = fonte_invaders.render('continue?' ,1, (cor_amarela))

        tela.blit(text, (350, 100))
        tela.blit(text2,(290, 160))

        x = int(x) - cronometro(1)
        x = str(x)
        pygame.display.update()


    pygame.quit()

continuar()