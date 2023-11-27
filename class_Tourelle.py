import pygame
from pygame import *
from pygame.locals import *
from random import random
#Une tourelle placée au sol à droite doit tirer sur les divisions. Elle le fait à raison d’une salve de 3
#tirs par seconde sur les 3 plus proches cibles par ordre de priorité en fonction de la distance.
#Un tir de tourelle doit être représenté par un trait continu pendant 0,1 seconde, il a 50 % de
#chance de toucher la division.
#Une division touchée par un tir disparaît.
ROUGE = (255, 0, 0)
BLANC = (255, 255, 255)
class Tourelle():

    def __init__(self,fenetre):
      
        self.fenetre = fenetre #doit tojours etre la fenetre
        self.fenetre_rect = fenetre.get_rect()
        self.temps_tir=0
        self.delai_tir=333 #3 tirs par seconde
        self.duree_tir=100 # le tir apparait pendant 0.1 sec
        self.temps_derniere_tir=0 # temps depuis le dernier tir
        self.collition=False
      

        
    #implementer tri 
    
    def tir(self,position_tir, firework):
       
        temps_actuel=pygame.time.get_ticks()
                 
        if temps_actuel - self.temps_tir > self.delai_tir: # attendre 333 milisecondes entre chaque tir

            self.position=position_tir
            self.positionX = firework.positionX
            self.positionY = firework.positionY
            self.rect= firework.circle
            self.circle_radius = firework.circle_radius

            tir = pygame.draw.line(self.fenetre,ROUGE,self.position,(self.positionX, self.positionY))
            pygame.display.update(tir)

            if tir.colliderect(self.rect):#collision avec la divition 

                self.collition=True

            if temps_actuel -self.temps_derniere_tir > self.duree_tir:#attendre 0.1 secondes entre chaque tir
                pass
                #p  ygame.display.update(pygame.draw.line(self.fenetre,BLANC,self.position,(self.positionX,self.positionY)))

            self.temps_tir=temps_actuel
            self.temps_derniere_tir=temps_actuel


    
    
            
        



