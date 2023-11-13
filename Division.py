import pygame



class Division:
    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY
        self.vitesse = -10 # vitesse initiale vers le haut
        self.gravity = 0.5
        # self.direction = direction
        self.couleur = (255, 0, 0)
        self.circle_radius = 10


    def move(self):
        self.vitesse += self.gravity
        self.positionY += self.vitesse





