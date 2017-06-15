#Teste
import pygame
from pygame.locals import *
from sys import *
import time
import os


pygame.init()


def animacao():
    def title_screen(screen):
        clock = pygame.time.Clock()
        title_name = 'title.png'
        title = pygame.image.load(title_name).convert()
        screen.blit(title, (0,0))
        pygame.display.update()
        time_passed = clock.tick(60)

    def movimento():
        screen = pygame.display.set_mode((900, 400))

        background_name = 'imagens/bg_scene.png'
        background = pygame.image.load(background_name).convert()

        audio = pygame.mixer.Sound('audios/cutsceneaudio.ogg')
        audio.play()

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

        pygame.display.set_caption("Hello World")

        clock = pygame.time.Clock()
        y = 500
        y2 = 600
        y3 = 600
        y_txt = 0
        y_bg = -6000
        c = 0
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

            if y > 220 or y <150:
                y -= 15

            if y < 150:
                y_txt +=13
            if y > 220 or y <50:
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
                print("a partir daqui sair da cutscene")

            pygame.display.update()
            time_passed = clock.tick(60)

    movimento()
animacao()



