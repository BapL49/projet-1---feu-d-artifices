import pygame
import math
from random import randint


class Division:
    def __init__(self, positionX, positionY, direction, fenetre):
        self.positionX = positionX
        self.positionY = positionY
        self.vitesseInitiale = randint(15, 30)
        self.direction = direction # angle (en radian) vers lequel se dirige la division
        self.gravite = 9.8
        self.couleur = (255, 0, 0)
        self.circle_radius = randint(5, 15)
        self.fenetre = fenetre
        
        self.circle = pygame.draw.circle(self.fenetre, self.couleur, (int(self.positionX), int(self.positionY)), self.circle_radius)
        
        # affiche un cercle à l'initialisation d'une instance de la classe
        pygame.display.update(pygame.draw.circle(self.fenetre, self.couleur, (int(self.positionX), int(self.positionY)), self.circle_radius))


    def move(self):
        dt = 0.1
        self.positionY += 0.5 * self.gravite * dt**2 + self.vitesseInitiale * math.sin(self.direction) * dt
        self.positionX += self.vitesseInitiale * math.cos(self.direction) * dt
        self.circle = pygame.draw.circle(self.fenetre, self.couleur, (int(self.positionX), int(self.positionY)), self.circle_radius)

    def update(self):
        self.move()
        pygame.display.update(pygame.draw.circle(self.fenetre, self.couleur, (int(self.positionX), int(self.positionY)), self.circle_radius))


