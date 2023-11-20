import pygame
from pygame import *
from pygame.locals import *
import time
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
        self.list_fireworks = list_fireworks#liste des instances de la class division
        self.delai=0.1

        list_firework_rect=[]
        

        global points#variable global des points
        points = 0 

        
    #implementer tri 
    
    def tir(self):
        #verifier que il y a de divisions dans la fenetre
        if self.list_fireworks == []:
            pass
        else:
            
            for firework in self.list_fireworks:
                firework_rect = firework.get_rect()
                condition = self.fenetre_rect.colliderect(firework_rect)
                
                while condition:
                    
                    for i in range(3):
                        
                        tir = pygame.draw.line(self.fenetre,ROUGE,self.position,(int(firework.positionX), int(firework.positionY)))

                        if tir.colliderect(firework_rect):
                            pygame.draw.circle(self.fenetre, BLANC , (int(firework.positionX), int(firework.positionY)), firework.circle_radius)
                            points+=1

                        time.sleep(0.1)
                        pygame.draw.line(self.fenetre,BLANC,self.position,(int(firework.positionX), int(firework.positionY)))
                    #3 tirs par seg
                    time.sleep(3.0)



