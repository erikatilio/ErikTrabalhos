import pygame, sys
from pygame.locals import  *
from random import randint

altura = 400
largura = 900
listaInimigos = []


class inimigo(pygame.sprite.Sprite):
    def __init__(self,posx,posy,distancia,imagemUm):
        pygame.sprite.Sprite.__init__(self)
        self.imagem1 = pygame.image.load(imagemUm)



        self.listaImagens = [self.imagem1]
        self.posImagem = 0
        self.ImagemAlien = self.listaImagens[self.posImagem]

        self.rect = self.ImagemAlien.get_rect()
        self.lista_disparoInimigo = []
        self.velocidade= 10
        self.rect.top = posy
        self.rect.left = posx
        self.configTempo = 1
        self.quantidadeDisparo = 5
        self.contador = 0
        self.direita = True
        self.maxDescida = self.rect.top + 40
        self.limitedireita = posx + distancia
        self.limiteEsquerda = posx - distancia

    def comportamento(self,tempo):
        self.__movimentos()
        self.__ataque()
        if self.configTempo < tempo:
            self.posImagem += 1
            self.configTempo += 1
            if self.posImagem > len(self.listaImagens)-1:
                self.posImagem = 0

    def __movimentos(self):
        if self.contador < 3:
            self.__movimentoLateral()
        else:
            self.__descendo()

    def __movimentoLateral(self):
        if self.direita == True:
            self.rect.left += self.velocidade
            if self.rect.left > self.limitedireita:
                self.direita = False
                self.contador += 1
        else:
            self.rect.left -= self.velocidade
            if self.rect.left < self.limiteEsquerda:
                self.direita = True

    def __descendo(self):
        if self.maxDescida == self.rect.top:
            self.contador = 0
            self.maxDescida = self.rect.top + 40

        else:
            self.rect.top += 1


    def colocar(self,superficie):
        self.ImagemAlien = self.listaImagens[self.posImagem]
        superficie.blit(self.ImagemAlien, self.rect)

    def __ataque(self):
        if (randint(3,300)<self.quantidadeDisparo):
            self.__disparo()

    def __disparo(self):
        x, y = self.rect.center
        minhaBala = bala(x, y, "imagens/alienBala.png", False)
        self.lista_disparoInimigo.append(minhaBala)

class bala(pygame.sprite.Sprite):
    def __init__(self,posx,posy,rota,personagem):
        pygame.sprite.Sprite.__init__(self)
        self.imagemBala = pygame.image.load(rota)
        self.rect = self.imagemBala.get_rect()
        self.velocidadeBala = 20
        self.rect.top = posy
        self.rect.left = posx
        self.disparoPersonagem = personagem

    def trajetoria(self):
        if self.disparoPersonagem == True:
            self.rect.top -= self.velocidadeBala
        else:
            self.rect.top += self.velocidadeBala

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

    def movimentoDireita(self):
        self.rect.right += self.velocidade
        self.__movimento()
    def movimentoEsquerda(self):
        self.rect.left -= self.velocidade
        self.__movimento()

    def __movimento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 900:
                self.rect.right = 900

    def disparo(self,x,y):
        minhaBala = bala(x,y,"imagens/naveBala.png",True)
        self.lista_disparo.append(minhaBala)

    def colocar(self,superficie):
        superficie.blit(self.imagemNave, self.rect)
def carregarInimigos():
    posx = 100
    for x in range(1,5):
        invasor = inimigo(posx,100,50,"imagens/alien01.png")
        listaInimigos.append(invasor)
        posx += 200
    posx = 100
    for x in range(1, 5):
        invasor = inimigo(posx, 0, 50,"imagens/alien02.png")
        listaInimigos.append(invasor)
        posx += 200
    posx = 100
    for x in range(1, 5):
        invasor = inimigo(posx, -100, 50,"imagens/alien03.png")
        listaInimigos.append(invasor)
        posx += 200

def jogo():
    pygame.init()

    tela = pygame.display.set_mode([largura,altura])
    pygame.display.set_caption("SPACE INVADERS")
    jogador = nave_espacial()
    imagemFundo = pygame.image.load("imagens/cenario.jpg")
    jogando = True
    carregarInimigos()
    relogio = pygame.time.Clock()
    #tiro = bala(largura / 2,altura - 20)
    audio = pygame.mixer.Sound("audios/intro4.ogg")
    audio.play()
    audio.set_volume(1)

    while True:
        relogio.tick(200)
        tempo = int(pygame.time.get_ticks()/1000)
        #tiro.trajetoria()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    jogador.movimentoEsquerda()
                elif event.key == K_RIGHT:
                    jogador.movimentoDireita()
                elif event.key == K_SPACE:
                    x,y = jogador.rect.center
                    jogador.disparo(x,y)

        tela.blit(imagemFundo,(0,0))
        jogador.colocar(tela)

        if len(jogador.lista_disparo) > 0:
            for x in jogador.lista_disparo:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.top < -10:
                    jogador.lista_disparo.remove(x)
                else:
                    for inimigo in listaInimigos:
                        if x.rect.colliderect(inimigo.rect):
                            listaInimigos.remove(inimigo)
                            jogador.lista_disparo.remove(x)

        if len(listaInimigos) > 0:
            for invasor in listaInimigos:
                invasor.comportamento(tempo)
                invasor.colocar(tela)
                if inimigo.rect.colliderect(jogador.rect):
                    print("perdeu")

                if len(invasor.lista_disparoInimigo) > 0:
                    for x in invasor.lista_disparoInimigo:
                        x.colocar(tela)
                        x.trajetoria()
                        if x.rect.colliderect(jogador.rect):
                            print("perdeu")
                        if x.rect.top > 900:
                            invasor.lista_disparoInimigo.remove(x)
                        else:
                            for disparo in jogador.lista_disparo:
                                if x.rect.colliderect(disparo.rect):
                                    jogador.lista_disparo.remove(disparo)
                                    inimigo.lista_disparoInimigo.remove(x)

        pygame.display.flip()
    pygame.quit()
jogo()
