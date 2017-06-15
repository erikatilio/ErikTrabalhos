import pygame, sys
from pygame.locals import *

altura = 400
largura = 900


class inimigo(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagem1 = pygame.image.load("imagens/alien01.png")
        self.imagem2 = pygame.image.load("imagens/alien02.png")
        self.imagem3 = pygame.image.load("imagens/alien03.png")
        self.imagem4 = pygame.image.load("imagens/nave2.png")

        self.listaimagens = [self.imagem1 , self.imagem2, self.imagem3, self.imagem4]
        self.posimagem = 0
        self.imagemalien = self.listaimagens[self.posimagem]

        self.rect = self.imagemalien.get_rect()
        self.lista_disparo = []
        self.velocidade = 20
        self.rect.top = posy
        self.rect.left = posx
        self.configTempo = 1

    def comportamento(self,tempo):
        if self.configTempo < tempo:
            self.posimagem += 1
            self.configTempo += 1
            if self.posimagem > len(self.listaimagens)-1:
                self.posimagem = 0

    def colocar(self,superficie):
        self.imagemalien = self.listaimagens[self.posimagem]
        superficie.blit(self.imagemalien, self.rect)

class bala(pygame.sprite.Sprite):


    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagemBala = pygame.image.load("imagens/naveBala.png")
        self.rect = self.imagemBala.get_rect()
        self.velocidadeBala = 20
        self.rect.top = posy
        self.rect.left = posx

    def trajetoria(self):
        self.rect.top -= self.velocidadeBala

    def colocar(self,superficie):
        superficie.blit(self.imagemBala, self.rect)


class nave_espacial(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagemNave = pygame.image.load("imagens/nave.png")
        self.rect = self.imagemNave.get_rect()
        self.rect.centerx = largura/2
        self.rect.centery = altura - 30

        self.lista_disparo = []
        self.vida = True
        self.velocidade = 25

    def movimentodireita(self):
        self.rect.right += self.velocidade
        self.__movimento()

    def movimentoesquerda(self):
        self.rect.left -= self.velocidade
        self.__movimento()

    def __movimento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 900:
                self.rect.right = 900

    def disparo(self, x, y):
        minhaBala = bala(x, y)
        self.lista_disparo.append(minhaBala)

    def colocar(self, superficie):
        superficie.blit(self.imagemNave, self.rect)


def jogo():
    pygame.init()

    tela = pygame.display.set_mode([largura,altura])
    pygame.display.set_caption("SPACE INVADERS")

    jogador = nave_espacial()
    invasor = inimigo(100,50)

    imagemfundo = pygame.image.load("imagens/cenario.jpg")
    jogando = True
    relogio = pygame.time.Clock()
    tiro = bala(largura / 2, altura - 20)
    audio = pygame.mixer.Sound("audios/intro4.ogg")
    audio.play()
    audio.set_volume(1)

    while True:
        relogio.tick(200)
        tempo = int(pygame.time.get_ticks()/1000)
        tiro.trajetoria()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    jogador.movimentoesquerda()
                elif event.key == K_RIGHT:
                    jogador.movimentodireita()
                elif event.key == K_SPACE:
                    x,y = jogador.rect.center
                    jogador.disparo(x,y)

        tela.blit(imagemfundo, (0, 0))
        jogador.colocar(tela)
        invasor.comportamento(tempo)
        invasor.colocar(tela)

        if len(jogador.lista_disparo) > 0:
            for x in jogador.lista_disparo:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.top < -10:
                    jogador.lista_disparo.remove(x)
        pygame.display.update()

jogo()
