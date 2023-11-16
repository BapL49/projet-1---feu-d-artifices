import pygame
import math
import time
from random import randint


class Division:
    def __init__(self, positionX, positionY, direction):
        self.positionX = positionX
        self.positionY = positionY
        self.vitesseInitiale = 5
        self.direction = math.radians(direction) # angle vers lequel se dirige la division
        self.accélération = 9.8
        self.couleur = (255, 0, 0)
        self.circle_radius = randint(5, 15)
        


    def move(self, dt):
        temps_ecoulee = dt
        self.positionY += 0.5 * self.accélération * temps_ecoulee**2 + self.vitesseInitiale * math.sin(self.direction) * temps_ecoulee
        self.positionX += self.vitesseInitiale * math.cos(self.direction) * temps_ecoulee



