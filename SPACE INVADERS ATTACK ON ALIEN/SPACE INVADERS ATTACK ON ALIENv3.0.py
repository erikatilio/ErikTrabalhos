# Teste
import pygame
from pygame.locals import *
from random import *
import sys
pygame.init()
# -----------------------------------------------ANIMAÇÃO---------------------------------------------------------------


def introduçao():

    def logo():
        screen = pygame.display.set_mode((900, 400))

        logo_name = 'imagens/logo.png'
        logo = pygame.image.load(logo_name).convert_alpha()

        presents_name = 'imagens/presents.png'
        presents = pygame.image.load(presents_name).convert_alpha()

        clock = pygame.time.Clock()

        pygame.display.set_caption("SPACE INVADERS: Attack on Aliens Edition")

        x = -400
        secs = 0
        y_txt = 50

        argument = True
        while argument is True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        argument = False

            screen.blit(pygame.Surface(screen.get_size()), (0, 0), )
            screen.blit(logo, (x, 50))
            screen.blit(presents, (0, y_txt))

            if x < 120:
                y_txt -= 3
                x += 40

            if x >= 120 and secs < 180:
                secs += 1

            if (secs/60) == 3:
                x += 40
                y_txt += 5

            if x >= 900:
                argument = False

            time_passed = clock.tick(60)
            pygame.display.update()

    def pygame_logo():

        screen = pygame.display.set_mode((900, 400))

        pygame_logo_name = 'imagens/pygame_logo.png'
        pygame_logo = pygame.image.load(pygame_logo_name).convert_alpha()

        clock = pygame.time.Clock()

        pygame.display.set_caption("SPACE INVADERS: Attack on Aliens Edition")

        pygame.mixer.music.load('audios/pygame.ogg')
        pygame.mixer.music.play()

        x = -400
        secs = 0

        argument = True
        while argument is True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        argument = False

            screen.blit(pygame.Surface(screen.get_size()), (0, 0), )
            screen.blit(pygame_logo, (x, 100))

            if x <= 200:
                x += 40

            if x >= 200 and secs < 180:
                secs += 1

            if (secs / 60) == 3:
                x += 40

            if x >= 900:
                argument = False

            time_passed = clock.tick(60)
            pygame.display.update()

    def animacao():
        screen = pygame.display.set_mode((900, 400))

        pygame.mixer.music.load('audios/cutsceneaudio.ogg')
        pygame.mixer.music.play()

        background_name = 'imagens/bg_scene.png'
        background = pygame.image.load(background_name).convert()

        ship_filename = 'imagens/nave.png'
        ship = pygame.image.load(ship_filename).convert_alpha()

        text_name = 'imagens/text.png'
        text = pygame.image.load(text_name).convert_alpha()

        enemy_filename = 'imagens/alien01.png'
        enemy = pygame.image.load(enemy_filename).convert_alpha()

        enemy2_filename = 'imagens/alien02.png'
        enemy2 = pygame.image.load(enemy2_filename).convert_alpha()

        enemy3_filename = 'imagens/alien03.png'
        enemy3 = pygame.image.load(enemy3_filename).convert_alpha()

        enemy4_filename = 'imagens/nave2.png'
        enemy4 = pygame.image.load(enemy4_filename).convert_alpha()

        pygame.display.set_caption("SPACE INVADERS: Attack on Aliens Edition")

        clock = pygame.time.Clock()
        y = 500
        y2 = 600
        y3 = 600
        y_txt = 0
        y_bg = -6000
        c = 0
        contador = 0
        cronometro = 0

        argument = True
        while argument is True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        argument = False

            screen.blit(pygame.Surface(screen.get_size()), (0, 0),)
            screen.blit(background, (0, y_bg))
            screen.blit(ship, (416, y))
            screen.blit(enemy, (600, y2))
            screen.blit(enemy2, (212, y2))
            screen.blit(enemy3, (12, y3))
            screen.blit(enemy4, (810, y3))

            if y > 220 or y < 150:
                y -= 15

            if y < 150:
                y_txt += 13

            if y > 220 or y < 50:
                y2 -= 12
                y3 -= 15

            if y < 220 or y < 150:
                screen.blit(text, (0, y_txt))

                y -= 0.15
                y2 -= 0.30
                y3 -= 0.40

            if y_bg <= 200:
                y_bg += 50

            if y_bg >= 200 and c < 2:
                y_bg = -6000
                c += 1

            if y < -2500:
                menu()

            time_passed = clock.tick(60)
            pygame.display.update()

    logo()
    pygame_logo()
    animacao()
    pygame.mixer.music.stop()


def creditos():
    screen = pygame.display.set_mode((900, 400))

    cor_yell = (255, 255, 0)

    creditos_name = 'imagens/creditos.png'
    creditos = pygame.image.load(creditos_name).convert_alpha()

    background_name = 'imagens/bg_scene.png'
    background = pygame.image.load(background_name).convert()

    clock = pygame.time.Clock()

    pygame.display.set_caption("SPACE INVADERS: Attack on Aliens Edition")

    pygame.mixer.music.stop()
    pygame.mixer.music.load('audios/creditos.ogg')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

    y_cd = 400
    y_bg = -6000

    argument = True

    while argument is True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    menu()

        screen.blit(pygame.Surface(screen.get_size()), (0, 0), )
        screen.blit(background, (0, y_bg))
        screen.blit(creditos, (0, y_cd))
        pygame.font.init()
        fonte_name = 'fonte/cosmic.ttf'
        fonte_presstback = pygame.font.Font(fonte_name, 10)
        press_to_back = fonte_presstback.render("Pressione Espaco para voltar", 1, (cor_yell))
        screen.blit(press_to_back, (0, 0))

        if y_bg <= 200:
            y_bg += 40

        if y_bg >= 200:
            y_bg = -6000

        y_cd -= 0.5

        if y_cd < -1926:
            menu()

        time_passed = clock.tick(60)
        pygame.display.update()


def loading():
    screen = pygame.display.set_mode((900, 400))

    load_name = 'imagens/load.png'
    load = pygame.image.load(load_name).convert_alpha()

    loading2_name = 'imagens/loading2.png'
    loading2 = pygame.image.load(loading2_name).convert_alpha()

    clock = pygame.time.Clock()

    pygame.display.set_caption("SPACE INVADERS: Attack on Aliens Edition")

    x = -400

    argument = True

    while argument is True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        screen.blit(pygame.Surface(screen.get_size()), (0, 0), )
        screen.blit(loading2, (x, 26))
        screen.blit(load, (0, 0))
        x += 1
        if x == -13:
            argument = False

        time_passed = clock.tick(60)
        pygame.display.update()


def instrucoes():
    pygame.init()
    tela = pygame.display.set_mode([900, 400])
    pygame.display.set_caption("SPACE INVADERS")
    pygame.font.init()

    background_name = 'imagens/background_title.png'
    background = pygame.image.load(background_name).convert()
    y_bg = 0

    fonte_cosmic = 'fonte/cosmic.ttf'
    titlefont = pygame.font.Font(fonte_cosmic, 55)
    textfont = pygame.font.Font(fonte_cosmic, 20)

    white = (255, 255, 255)
    black = (0, 0, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 255)

    sair = False
    while sair is not True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sair = True

        tela.fill(black)
        tela.blit(background, (0, y_bg))
        title = titlefont.render("INSTRUCOES PARA NOOBS", True, yellow)
        title_shade = titlefont.render("INSTRUCOES PARA NOOBS", True, white)
        text = textfont.render("> Mover-se para os lados = Setas direcionais", True, white)
        text_shade = textfont.render("> Mover-se para os lados = Setas direcionais", True, blue)
        text1 = textfont.render("> Atirar = Espaco", True, white)
        text1_shade = textfont.render("> Atirar = Espaco", True, blue)
        text2 = textfont.render("> Se voce for muito ruim, aperte Alt + F4 ;)", True, white)
        text2_shade = textfont.render("> Se voce for muito ruim, aperte Alt + F4 ;)", True, blue)
        text_sair = textfont.render("Pressione espaco para voltar ao menu", True, white)

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


# -----------------------------------------------MENU-------------------------------------------------------------------


def menu():
    pygame.init()
    tela = pygame.display.set_mode([900, 400])
    pygame.display.set_caption("SPACE INVADERS: Attack on Aliens Edition")
    pygame.font.init()

    # BackGround
    background_name = 'imagens/background_title.png'
    background = pygame.image.load(background_name).convert()
    y_bg = 0

    # fontes
    fonte_name = 'fonte/cosmic.ttf'
    fonte_space = pygame.font.SysFont(fonte_name, 55)
    fonte_invaders = pygame.font.Font(fonte_name, 55)
    fonte_play = pygame.font.Font(fonte_name, 20)
    fonte_intrucao = pygame.font.Font(fonte_name, 20)
    fonte_credito = pygame.font.Font(fonte_name, 20)
    fonte_logo = pygame.font.Font(fonte_name, 10)
    fonte_quit = pygame.font.Font(fonte_name, 20)

    # musica
    music = 'audios/menu_theme.ogg'
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.25)

    # cores
    cor_branco = (255, 255, 255)
    cor_preto = (0, 0, 0)
    cor_amarela = (255, 255, 000)
    sair = False

    # while para funcoes

    while sair is not True:
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
                        game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] >= 310 and mouse[1] >= 300:
                    if mouse[0] <= 430 and mouse[1] <= 320:
                        instrucoes()


    # adicionando fontes

        tela.fill(cor_preto)
        tela.blit(background, (0, y_bg))
        text = fonte_invaders.render('SPACE ', 1, (cor_amarela))
        text2 = fonte_invaders.render('INVADERS', 1, (cor_amarela))
        text_shade = fonte_invaders.render('SPACE ', 1, (cor_branco))
        text2_shade = fonte_invaders.render('INVADERS', 1, (cor_branco))
        edtitle = fonte_play.render('Attack on Alien Edition', 1, (cor_amarela))
        text3 = fonte_play.render('Jogar', 1, (cor_amarela))
        text4 = fonte_intrucao.render('Instrucoes', 1, (cor_amarela))
        text5 = fonte_credito.render('Creditos', 1, (cor_amarela))
        text6 = fonte_quit.render('Sair', 1, (cor_amarela))
        text_logo = fonte_logo.render('COMMIT GROUP 2017 ', 1, (cor_amarela))

        tela.blit(text_shade, (348, 98))
        tela.blit(text, (350, 100))
        tela.blit(text2_shade, (288, 158))
        tela.blit(text2, (290, 160))
        tela.blit(edtitle, (278, 210))
        tela.blit(text_logo, (760, 390))
        tela.blit(text3, (210, 300))
        tela.blit(text4, (310, 300))
        tela.blit(text5, (475, 300))
        tela.blit(text6, (620, 300))
        y_bg -= 0.05
        if y_bg < -1600:
            pygame.mixer.music.stop()
            introduçao()
            y_bg = 0

        # variavel para pegar a posicao do cursor
        mouse = pygame.mouse.get_pos()

        # variavel para atualizar o display
        pygame.display.update()
    pygame.quit()


# ---------------------------------------------------------------CONTINUE-----------------------------------------------
def continuar():

    pygame.init()
    tela = pygame.display.set_mode([900, 400])
    pygame.display.set_caption("SPACE INVADERS: Attack on Aliens Edition")
    pygame.font.init()

    clock = pygame.time.Clock()

    # BackGround
    background_name = 'imagens/background_title.png'
    background = pygame.image.load(background_name).convert()
    y_bg = 0

    # fontes
    fonte_name = 'fonte/cosmic.ttf'
    fonte_gover = pygame.font.Font(fonte_name, 55)
    fonte_continue = pygame.font.Font(fonte_name, 55)
    fonte_number = pygame.font.Font(fonte_name, 80)

    # musica
    music = pygame.mixer.music.load('audios/gameover.ogg')
    pygame.mixer.music.play()
    # cores
    cor_branco = (255, 255, 255)
    cor_preto = (0, 0, 0)
    cor_amarela = (255, 255, 000)
    sair = False

    # while para funcoes
    x = "10"
    frame = 0
    secs = 0
    number_x = 400
    while sair is not True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        # adicionando fontes

        tela.fill(cor_preto)
        tela.blit(background, (0, y_bg))
        text = fonte_gover.render('GAME OVER CHAMPS', 1, (cor_amarela))
        text2 = fonte_continue.render('TENTAR NOVAMENTE?', 1, (cor_amarela))
        text3 = fonte_number.render(x, 1, (cor_amarela))

        tela.blit(text, (120, 100))
        tela.blit(text2, (100, 160))
        tela.blit(text3, (number_x, 220))

        frame += 1
        y_bg -= 0.5
        if frame == 100:
            x = str(int(x) - 1)
            frame = 0
            if number_x == 400:
                number_x += 25

        if int(x) == 0:
            menu()

        # variavel para atualizar o display
        pygame.display.update()
        time_passed = clock.tick(60)
    pygame.quit()

# -----------------------------------------------JOGO-------------------------------------------------------------------


def game():
    altura = 400
    largura = 900
    lista_inimigos = []

    def reiniciar(tecla, comando):
        if tecla and KMOD_CTRL:
            if tecla[K_r]:
                jogo()

    def para_tudo():
        for inimigo in lista_inimigos:
            for disparo in inimigo.lista_disparo_inimigo:
                inimigo.lista_disparo_inimigo.remove(disparo)
            inimigo.venceu = True

    class inimigo(pygame.sprite.Sprite):
        def __init__(self, posx, posy, distancia, imagem_um, imagem_dois):
            pygame.sprite.Sprite.__init__(self)
            self.imagem1 = pygame.image.load(imagem_um)
            self.imagem2 = pygame.image.load(imagem_dois)

            self.lista_imagens = [self.imagem1, self.imagem2]
            self.pos_imagem = 0
            self.imagem_alien = self.lista_imagens[self.pos_imagem]

            self.rect = self.imagem_alien.get_rect()
            self.lista_disparo_inimigo = []
            self.velocidade = 1
            self.rect.top = posy
            self.rect.left = posx
            self.configTempo = 1
            self.quantidadedisparo = 1
            self.contador = 0
            self.direita = True
            self.maxDescida = self.rect.top
            self.limitedireita = posx + distancia
            self.limite_esquerda = posx - distancia
            self.venceu = False

        def comportamento(self, tempo):
            if self.venceu is False:
                self.__movimentos()
                self.__ataque()
                if self.configTempo < tempo:
                    self.pos_imagem += 1
                    self.configTempo += 1
                    if self.pos_imagem > len(self.lista_imagens)-1:
                        self.pos_imagem = 0

        def __movimentos(self):
            if self.contador < 1:
                self.__movimento_lateral()
            else:
                self.__descendo()

        def __movimento_lateral(self):
            if self.direita is True:
                self.rect.left += self.velocidade
                if self.rect.left > self.limitedireita:
                    self.direita = False
                    self.contador += 1
            else:
                self.rect.left -= self.velocidade
                if self.rect.left < self.limite_esquerda:
                    self.direita = True

        def __descendo(self):
            if self.maxDescida == self.rect.top:
                self.contador = 0
                self.maxDescida = self.rect.top + 8

            else:
                self.rect.top += 1

        def colocar(self, superficie):
            self.imagem_alien = self.lista_imagens[self.pos_imagem]
            superficie.blit(self.imagem_alien, self.rect)

        def __ataque(self):
            if (randint(0, 2000) < self.quantidadedisparo):
                self.__disparo()

        def __disparo(self):
            x, y = self.rect.center
            minhaBala = bala(x, y, "imagens/alienBala.png", False)
            self.lista_disparo_inimigo.append(minhaBala)

    class bala(pygame.sprite.Sprite):
        def __init__(self, posx, posy, rota, personagem):
            pygame.sprite.Sprite.__init__(self)
            self.imagemBala = pygame.image.load(rota)
            self.rect = self.imagemBala.get_rect()
            self.velocidade_bala = 4
            self.rect.top = posy
            self.rect.left = posx
            self.disparo_personagem = personagem

        def trajetoria(self):
            if self.disparo_personagem is True:
                self.rect.top -= self.velocidade_bala
            else:
                self.rect.top += self.velocidade_bala

        def colocar(self, superficie):
            superficie.blit(self.imagemBala, self.rect)

    class nave_espacial(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.imagem_nave = pygame.image.load("imagens/nave.png")
            self.imagem_explosao = pygame.image.load("imagens/explosao.png")
            self.boom = pygame.mixer.Sound("audios/boom.ogg")

            self.rect = self.imagem_nave.get_rect()
            self.rect.centerx = largura/2
            self.rect.centery = altura - 30

            self.lista_disparo = []
            self.vida = True
            self.velocidade = 40

        def destruicao(self):
            self.vida = False
            self.velocidade = 0
            self.imagem_nave = self.imagem_explosao

        def movimento_direita(self):
            self.rect.right += self.velocidade
            self.__movimento()

        def movimento_esquerda(self):
            self.rect.left -= self.velocidade
            self.__movimento()

        def __movimento(self):
            if self.vida is True:
                if self.rect.left <= 0:
                    self.rect.left = 0
                elif self.rect.right > 900:
                    self.rect.right = 900

        def disparo(self, x, y):
            if self.vida is True:
                minha_bala = bala(x, y, "imagens/naveBala.png", True)
                self.lista_disparo.append(minha_bala)

        def colocar(self, superficie):
            superficie.blit(self.imagem_nave, self.rect)

    def carregar_inimigos():
        posx = 15
        for x in range(1, 10):
            invasor = inimigo(posx, -50, 5, "imagens/alien01.png", "imagens/alien01(2).png")
            lista_inimigos.append(invasor)
            posx += 100
        posx = 15
        for x in range(1, 10):
            invasor = inimigo(posx, -180, 5, "imagens/alien02.png", "imagens/alien02(2).png")
            lista_inimigos.append(invasor)
            posx += 100
        posx = 15
        for x in range(1, 10):
            invasor = inimigo(posx, -310, 5, "imagens/alien03.png", "imagens/alien03(2).png")
            lista_inimigos.append(invasor)
            posx += 100
        posx = 8
        for x in range(1, 10):
            invasor = inimigo(posx, -410, 5, "imagens/nave2.png", "imagens/nave2(2).png")
            lista_inimigos.append(invasor)
            posx += 100

    def jogo():
        pygame.init()

        tela = pygame.display.set_mode([largura, altura])
        pygame.display.set_caption("SPACE INVADERS: Attack on Aliens Edition")
        jogador = nave_espacial()
        imagemFundo = pygame.image.load("imagens/cenario.jpg")
        fim = pygame.image.load("imagens/GameOver.png")
        win = pygame.image.load("imagens/win.png")
        som_morte = pygame.mixer.Sound('audios/boom.ogg')
        win_music = pygame.mixer.Sound('audios/youwin.ogg')
        lista_music = ['audios/intro.ogg', 'audios/intro2.ogg', 'audios/intro3.ogg', 'audios/intro4.ogg']

        jogando = True
        carregar_inimigos()
        relogio = pygame.time.Clock()
        pygame.mixer.music.stop()
        number = randint(0, 3)
        shot = pygame.mixer.Sound('audios/shot.ogg')
        hurt = pygame.mixer.Sound('audios/hurt.ogg')
        audio = pygame.mixer.Sound(lista_music[number])
        audio.play()
        audio.set_volume(0.5)
        tiros = 0
        secs = 0
        music = 0

        while True:
            relogio.tick(60)
            tempo = int(pygame.time.get_ticks()/1000)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        jogador.movimento_esquerda()
                    elif event.key == K_RIGHT:
                        jogador.movimento_direita()
                    elif event.key == K_SPACE:
                        if tiros < 1:
                            tiros += 1
                            shot.play()
                            x, y = jogador.rect.center
                            jogador.disparo(x - 7, y - 60)

            if tiros == 1:
                secs += 1
                if secs == 60:
                    tiros = 0
                    secs = 0

            tela.blit(imagemFundo, (0, 0))
            jogador.colocar(tela)

            if len(jogador.lista_disparo) > 0:
                for x in jogador.lista_disparo:
                    x.colocar(tela)
                    x.trajetoria()
                    if x.rect.top < -10:
                        jogador.lista_disparo.remove(x)
                    else:
                        for inimigo in lista_inimigos:
                            if x.rect.colliderect(inimigo.rect):
                                hurt.play()
                                lista_inimigos.remove(inimigo)
                                jogador.lista_disparo.remove(x)

            if len(lista_inimigos) == 0:
                reiniciar(pygame.key.get_pressed(), pygame.key.get_mods())
                audio.stop()
                tela.blit(win, (0, 0))
                if music == 0:
                    win_music.play()
                    music += 1
                    para_tudo()

            if len(lista_inimigos) > 0:
                for invasor in lista_inimigos:
                    invasor.comportamento(tempo)
                    invasor.colocar(tela)
                    if invasor.rect.colliderect(jogador.rect):
                        jogando = False
                        para_tudo()

                    if len(invasor.lista_disparo_inimigo) > 0:
                        for x in invasor.lista_disparo_inimigo:
                            x.colocar(tela)
                            x.trajetoria()
                            if x.rect.colliderect(jogador.rect):
                                jogando = False
                            if x.rect.top > 900:
                                invasor.lista_disparo_inimigo.remove(x)

                            else:
                                for disparo in jogador.lista_disparo:
                                    if x.rect.colliderect(disparo.rect):
                                        jogador.lista_disparo.remove(disparo)
                                        invasor.lista_disparo_inimigo.remove(x)
            if jogando is False:
                para_tudo()
                audio.stop()
                continuar()

            pygame.display.flip()

    jogo()

loading()
introduçao()
menu()

