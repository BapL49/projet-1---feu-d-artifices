import pygame



class CompteurPoints:
    def __init__(self, positionX, positionY, fenetre) :
        self.points = 0
        self.positionX = positionX
        self.positionY = positionY
        self.fenetre = fenetre
        
        # Affichage du compteur de points
        pygame.font.init()

        self.font = pygame.font.SysFont('comic Sans MS', 20)
        self.compteur = self.font.render(f'POINTS : {self.points}', False, (255, 255, 255))

        self.fenetre.blit(self.compteur, (self.positionX, self.positionY))
        pygame.display.flip()


    def ajouterPoints(self):
        self.points += 10
        
        self.compteur = self.font.render(f'POINTS : {self.points}', False, (255, 255, 255))
        self.fenetre.blit(self.compteur, (self.positionX, self.positionY))

        pygame.display.flip()    
