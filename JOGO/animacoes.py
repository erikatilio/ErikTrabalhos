#Teste
import pygame
from pygame.locals import *
from sys import *
import time
import os
from cronometro import *

pygame.init()


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
        while argument == True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            screen.blit(pygame.Surface(screen.get_size()), (0, 0), )
            screen.blit(logo, (x, 50))
            screen.blit(presents, (0, y_txt))

            if x <= 200:
                x += 43
                y_txt -= 5

            if x >= 200 and secs == 0:
                secs = cronometro(3)

            if secs == 3:
                x += 43
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
        while argument == True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            screen.blit(pygame.Surface(screen.get_size()), (0, 0), )
            screen.blit(pygame_logo, (x, 100))

            if x <= 285:
                x += 43

            if x >= 285 and secs == 0:
                secs = cronometro(3)
            if secs == 3:
                x += 43
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
        while argument == True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
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
                y_txt +=13

            if y > 220 or y < 50:
                y2 -= 12
                y3 -= 15

            if y < 220 or y < 150:
                screen.blit(text, (0, y_txt))

                y -= 0.15
                y2 -= 0.30
                y3 -= 0.40

            if y_bg <= 200:
                y_bg += 40

            if y_bg >= 200 and c < 2:
                y_bg = -6000
                c += 1

            if y < -3001.3000000000134:
                argument = False

            time_passed = clock.tick(60)
            pygame.display.update()

    logo()
    pygame_logo()
    animacao()
    pygame.mixer.music.stop()
    pygame.time.wait(350)


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

    y_cd = 400
    y_bg = -6000

    argument = True

    while argument == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    argument = False

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

        if y_cd < -1926.5:
            argument = False

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

    while argument == True:
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