import pygame
from pygame import *
from pygame.locals import *
from time import sleep
from random import random
#Une tourelle placée au sol à droite doit tirer sur les divisions. Elle le fait à raison d’une salve de 3
#tirs par seconde sur les 3 plus proches cibles par ordre de priorité en fonction de la distance.
#Un tir de tourelle doit être représenté par un trait continu pendant 0,1 seconde, il a 50 % de
#chance de toucher la division.
#Une division touchée par un tir disparaît.
ROUGE = (255, 0, 0)
BLANC = (255, 255, 255)
class Tourelle():

    def __init__(self,fenetre,position,list_fireworks ):
      
        self.fenetre = fenetre #doit tojours etre la fenetre
        self.fenetre_rect = fenetre.get_rect()
        self.position = position #position de debut du tir
        self.list_fireworks = self.list_fireworks#liste des instances de la class division
        self.delai=0.1
        
    #implementer tri 
    
    def tir(self):
        #verifier que il y a de divisions dans la fenetre
        condition = self.fenetre_rect.colliderect(firework)

        for firework in self.list_fireworks:
            
            while condition:
                
                for i in range(3):
                    
                    tir = pygame.draw.line(self.fenetre,ROUGE,self.position,(int(firework.positionX), int(firework.positionY)))

                    if tir.colliderect(self.cible):
                        pygame.draw.circle(self.fenetre, BLANC , (int(firework.positionX), int(firework.positionY)), firework.circle_radius)
                
                    sleep(0.1)
                    pygame.draw.line(self.fenetre,BLANC,self.position,(int(firework.positionX), int(firework.positionY)))
                #3 tirs par seg
                sleep(3.0)



