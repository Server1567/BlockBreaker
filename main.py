#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import pygame
import sys
from pygame.locals import *
 
# Constantes o Variables
color = (234,234,234)
WIDTH = 850
HEIGHT = 480
window = pygame.display.set_mode((WIDTH,HEIGHT))
 
# Clases
# ---------------------------------------------------------------------

class Bola(pygame.sprite.Sprite):
    """Comportamiento de la Bola"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("Imagenes/ball.png", True) # Ignored
        self.rect = self.image.get_rect()                  # Ignored
        self.rect.centerx = 425
        self.rect.centery = 450
        self.speed = [0.2, -0.2]
 

    def movimiento(self, time):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT or self.rect.colliderect(player.rect):
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time

    def destroy(self):
        if self.rect.colliderect(block1A):
            block1A.remove()


    def dibujar(self):
        pygame.draw.circle(window,(255,255,255),(self.rect.centerx, self.rect.centery),8)


# ---------------------------------------------------------------------

class Player(pygame.sprite.Sprite):
    """Comportamiento del Jugador"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/player.png")
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT -10
        self.speed = 0
        self.aceleracion = 7
        
    def movimiento(self, direccion):
        if direccion == "NO":
            self.speed = 0

        elif direccion == "IZQUIERDA":
            self.speed = -self.aceleracion

        elif direccion == "DERECHA":
            self.speed = self.aceleracion
    

    def actualizar(self):
        self.rect.centerx += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 850:
            self.rect.right = 850


    def dibujar(self):
        window.blit(self.image, self.rect)

# ---------------------------------------------------------------------

class Block(pygame.sprite.Sprite):
    """Comportamiento de los Bloques"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Imagenes/ball.png")
        self.rect = self.image.get_rect()
        self.centerx = WIDTH / 2
        self.centery = HEIGHT / 2
        self.unbroken = True
    
    def __destroying(self):
        pass

    def dibujar(self, posX, posY):
        pygame.draw.rect(window,color,(posX,posY,75,20))
        self.__destroying()


# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------

def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image


# --------------------------------------------------------------------- 
 
def main():
    pygame.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("BlockBreaker")

    icon = pygame.image.load("Imagenes/ball.ico")
    pygame.display.set_icon(icon)


    # Objetos principales
    global bola
    bola = Bola()
    global player
    player = Player()


# ---------------------------------------------------------------------
 
# Creación de Bloques | START
# ---------------------------------------------------------------------
    
    block1A = Block()
    block2A = Block()
    block3A = Block()
    block4A = Block()
    block5A = Block()
    block6A = Block()
    block7A = Block()
    block8A = Block()
    block9A = Block()
    block10A = Block()

    block1B = Block()
    block2B = Block()
    block3B = Block()
    block4B = Block()
    block5B = Block()
    block6B = Block()
    block7B = Block()
    block8B = Block()

    block1C = Block()
    block2C = Block()
    block3C = Block()
    block4C = Block()
    block5C = Block()
    block6C = Block()

    block1D = Block()
    block2D = Block()
    block3D = Block()
    block4D = Block()

    block1E = Block()
    block2E = Block()

    block1F = Block()

    blocks = [block1A, block2A, block3A, block4A, block5A, block6A, block7A, block8A, block9A,block10A,
              block1B, block2B, block3B, block4B, block5B, block6B, block7B, block8B,
              block1C, block2C, block3C, block4C, block5C, block6C,
              block1D, block2D, block3D, block4D,
              block1E, block2E,
              block1F]

    blocks[0].remove()



# ---------------------------------------------------------------------
 
# Creación de Bloques | END
# ---------------------------------------------------------------------

 
    clock = pygame.time.Clock()

 
    while True:
        window.fill((90,90,90))
        time = clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == QUIT:
            	pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    elif event.key == K_LEFT:
                        player.movimiento("IZQUIERDA")

                    elif event.key == K_RIGHT:
                        player.movimiento("DERECHA")

            elif event.type == KEYUP:
                    if event.key == K_LEFT:
                        player.movimiento("NO")

                    elif event.key == K_RIGHT:
                        player.movimiento("NO")



 
        bola.movimiento(time)
        bola.dibujar()
        player.actualizar()
        player.dibujar()


# ---------------------------------------------------------------------
 
# Renderización de Bloques | START
# ---------------------------------------------------------------------

        blocks[0].dibujar(20,165)
        blocks[1].dibujar(100,165)
        blocks[2].dibujar(180,165)
        blocks[3].dibujar(260,165)
        blocks[4].dibujar(340,165)
        blocks[5].dibujar(420,165)
        blocks[6].dibujar(500,165)
        blocks[7].dibujar(580,165)
        blocks[8].dibujar(660,165)
        blocks[9].dibujar(740,165)

        blocks[10].dibujar(100,135)
        blocks[11].dibujar(180,135)
        blocks[12].dibujar(260,135)
        blocks[13].dibujar(340,135)
        blocks[14].dibujar(420,135)
        blocks[15].dibujar(500,135)
        blocks[16].dibujar(580,135)
        blocks[17].dibujar(660,135)

        blocks[18].dibujar(180,105)
        blocks[19].dibujar(260,105)
        blocks[20].dibujar(340,105)
        blocks[21].dibujar(420,105)
        blocks[22].dibujar(500,105)
        blocks[23].dibujar(580,105)

        blocks[24].dibujar(260,75)
        blocks[25].dibujar(340,75)
        blocks[26].dibujar(420,75)
        blocks[27].dibujar(500,75)

        blocks[28].dibujar(340,45)
        blocks[29].dibujar(420,45)

        blocks[30].dibujar(380,15)

# ---------------------------------------------------------------------
 
# Renderización de Bloques | END
# ---------------------------------------------------------------------
    
    	pygame.display.update()
 
main()

"""Tuve problemas al crear un Bucle que iterara los bloques para crear más rapido,
 así que lo hize de modo rudo. xD
 """