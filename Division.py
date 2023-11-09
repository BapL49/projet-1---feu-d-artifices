import pygame



class Division:
    def __init__(self, positionX, positionY, direction, fenetre):
        self.positionX = positionX
        self.positionY = positionY
        self.position = pygame.math.Vector2((positionX, positionY))
        self.vitesse = pygame.math.Vector2(50,50) # entier représentant la vitesse de la division
        self.acceleration = pygame.math.Vector2(0,0)
        self.direction = direction
        self.couleur = (255, 0, 0)
        self.fenetre = fenetre
        self.circle_radius = 10

        self.cercle = pygame.draw.circle(self.fenetre, self.couleur, (self.position.x, self.position.y), self.circle_radius)
        pygame.display.update(self.cercle)


    def move(self):
        for i in range(60):
            self.position += self.vitesse
            pygame.display.update(self.cercle)




    def gravity(self):
        pass
    

