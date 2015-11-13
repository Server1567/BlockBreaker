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
        self.centerx = WIDTH / 2
        self.centery = HEIGHT / 2
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
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        
        
    def destruction(self):
        pass

    def dibujar(self, posX, posY):
        pygame.draw.rect(window,color,(posX,posY,75,20))

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

    icon = pygame.image.load("Imagenes/ball.png")
    pygame.display.set_icon(icon)

    # Objetos principales
    bola = Bola()
    global player
    player = Player()

# ---------------------------------------------------------------------
 
# Creación de Bloques | START
# ---------------------------------------------------------------------

    block1A = Block(20,165)
    block2A = Block(100,165)
    block3A = Block(180,165)
    block4A = Block(260,165)
    block5A = Block(340,165)
    block6A = Block(420,165)
    block7A = Block(500,165)
    block8A = Block(580,165)
    block9A = Block(660,165)
    block10A = Block(740,165)

    block1B = Block(100,135)
    block2B = Block(180,135)
    block3B = Block(260,135)
    block4B = Block(340,135)
    block5B = Block(420,135)
    block6B = Block(500,135)
    block7B = Block(580,135)
    block8B = Block(660,135)

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

        block1A.dibujar(20,165)
        block2A.dibujar(100,165)
        block3A.dibujar(180,165)
        block4A.dibujar(260,165)
        block5A.dibujar(340,165)
        block6A.dibujar(420,165)
        block7A.dibujar(500,165)
        block8A.dibujar(580,165)
        block9A.dibujar(660,165)
        block10A.dibujar(740,165)

        block1B.dibujar(100,135)
        block2B.dibujar(180,135)
        block3B.dibujar(260,135)
        block4B.dibujar(340,135)
        block5B.dibujar(420,135)
        block6B.dibujar(500,135)
        block7B.dibujar(580,135)
        block8B.dibujar(660,135)

# ---------------------------------------------------------------------
 
# Renderización de Bloques | END
# ---------------------------------------------------------------------

    	pygame.display.update()
 
main()
