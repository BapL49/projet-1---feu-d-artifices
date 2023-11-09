import pygame


class Division:
    def __init__(self, positionX, positionY, direction, fenetre):
        self.positionX = positionX
        self.positionY = positionY
        self.vitesse = 10 # entier représentant la vitesse de la division
        self.direction = direction
        self.couleur = (255, 0, 0)
        self.fenetre = fenetre
        self.circle_radius = 10

        cercle = pygame.draw.circle(self.fenetre, self.couleur, (self.positionX, self.positionY), self.circle_radius)
        
        pygame.display.update(cercle)
    

    def update(self):
        pass



    def gravity(self):
        pass
    

