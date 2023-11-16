import pygame
import math
import time
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
        self.temps = time.time()


    def move(self):
        self.positionY = self.accélération * self.temps**2 + self.vitesse * self.temps + self.positionY
        





