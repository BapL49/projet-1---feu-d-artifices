import pygame
import array 
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
      

        
    #implementer tri =https://www.geeksforgeeks.org/python-program-for-merge-sort/ et https://www.geeksforgeeks.org/python-arrays/
    
    def tri(self,list_fireworks):
        pass
    
    def tir_vers_firework(self,position_tir, firework):
       
        temps_actuel=pygame.time.get_ticks()
        self.collition=False    
        if temps_actuel - self.temps_tir > self.delai_tir: # attendre 333 milisecondes entre chaque tir
            
            self.position=position_tir
            self.positionX = firework.positionX
            self.positionY = firework.positionY
            self.rect= firework.circle
            

            tir = pygame.draw.line(self.fenetre,ROUGE,self.position,(self.positionX, self.positionY),5)
            

            if tir.colliderect(self.rect):#collision avec la divition 

                self.collition=True
                firework_touchee=firework

            if temps_actuel -self.temps_derniere_tir > self.duree_tir:#attendre 0.1 secondes entre chaque tir
                pygame.display.update(tir)

            self.temps_tir=temps_actuel
            self.temps_derniere_tir=temps_actuel

    def tir_vers_souris(self,position_tir):
        
        temps_actuel=pygame.time.get_ticks()
                 
        if temps_actuel - self.temps_tir > self.delai_tir: # attendre 333 milisecondes entre chaque tir
            
            self.position=position_tir
            self.coordinates=pygame.mouse.get_pos()
       
            tir = pygame.draw.line(self.fenetre,ROUGE,self.position,(self.coordinates))
            
        
            if temps_actuel -self.temps_derniere_tir > self.duree_tir:#attendre 0.1 secondes entre chaque tir
                pygame.display.update(tir)
                

            self.temps_tir=temps_actuel
            self.temps_derniere_tir=temps_actuel

    
    
class Canon(pygame.Surface):
    def __init__(self, parent, xpos, ypos, width, height):
      super(Canon, self).__init__(width, height)
      self.xpos = xpos
      self.ypos = ypos
      self.parent = parent

    def update(self, parent):
      parent.blit(self, (self.xpos, self.ypos))

    def rotate(self, angle):
      #(your rotation code goes here)
      pass