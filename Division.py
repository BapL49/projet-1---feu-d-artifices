import pygame
import math
from random import randint


class Division:
    def __init__(self, positionX, positionY, direction, fenetre):
        self.positionX = positionX
        self.positionY = positionY
        self.direction = direction # angle (en radian) vers lequel se dirige la division
        self.vitesseInitialeBase = 6 # constante vitesse de départ
        self.vitesseInitialeY = self.vitesseInitialeBase * math.sin(self.direction) #vitesse de départ Y
        self.vitesse = randint(8, 22) # vitesse 
        self.acceleration = 9.8
        self.couleur = (255, 0, 0)
        self.circle_radius = randint(5, 15)
        self.fenetre = fenetre
        
        self.circle = pygame.draw.circle(self.fenetre, self.couleur, (int(self.positionX), int(self.positionY)), self.circle_radius)
        
        # affiche un cercle à l'initialisation d'une instance de la classe
        pygame.display.update(self.circle)


    def move(self):
        dt = 0.1
        self.positionY += 0.5 * self.acceleration * dt**2 + self.vitesseInitialeY * dt
        self.positionX += 0.5 * self.acceleration * dt**2 + self.vitesse * self.vitesseInitialeBase * math.cos(self.direction) * dt
        self.circle = pygame.draw.circle(self.fenetre, self.couleur, (int(self.positionX), int(self.positionY)), self.circle_radius)
        self.vitesseInitialeY += self.vitesse


    def update(self):
        self.move() # calcule de la nouvelle position de la division
        pygame.display.update(self.circle) # actualisation de l'affichage de la division


