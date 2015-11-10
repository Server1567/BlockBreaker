#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import pygame
import sys
from pygame.locals import *
 
# Constantes o Variables
WIDTH = 850
HEIGHT = 480
window = pygame.display.set_mode((WIDTH,HEIGHT))
 
# Clases
# ---------------------------------------------------------------------

class Bola(pygame.sprite.Sprite):
    """Comportamiento de la Bola"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("Imagenes/ball.png", True)
        self.rect = self.image.get_rect()
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
            # ¿Cómo uso player.rect sin antes haberlo declarado?
            # ¿Hay una menera hacerlo?
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

    bola = Bola()
    player = Player()
 
    clock = pygame.time.Clock()

    velocidad = 10
 
    while True:
        window.fill((0,0,0))
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
    
    	pygame.display.update()
 
main()
