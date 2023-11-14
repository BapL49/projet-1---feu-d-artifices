import pygame
from random import randint


class Division:
    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY
        self.vitesse = randint(-10, 5) # vitesse initiale valeur négative -> déplacement vers le haut 
        self.accélération = 0.5
        self.direction = randint(-5, 5) # direction x de la division
        self.couleur = (255, 0, 0)
        self.circle_radius = randint(5, 15)


    def move(self):
        self.positionY += ((0.5 * self.accélération)**2) + self.vitesse
        self.positionX += ((0.5 * self.accélération)**2) + self.direction
        self.vitesse += self.accélération





