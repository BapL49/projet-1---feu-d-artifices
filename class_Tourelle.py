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

    def __init__(self,fenetre):
      
        self.fenetre = fenetre #doit tojours etre la fenetre
        self.fenetre_rect = fenetre.get_rect()
        global points#variable global des points
        points = 0 

        
    #implementer tri 
    
    def tir(self,position_tir, firework):
        self.position=position_tir
        self.positionX = firework.positionX
        self.positionY = firework.positionY
        self.circle_radius = firework.circle_radius
                    
        for i in range(3):

            tir = pygame.draw.line(self.fenetre,ROUGE,self.position,(self.positionX, self.positionY))

            if tir.colliderect():#collision avec la divition 
                pygame.draw.circle(self.fenetre, BLANC , (self.positionX, self.positionY), self.circle_Radius)
                points+=1

            time.sleep(0.1)
            pygame.draw.line(self.fenetre,BLANC,self.position,(self.positionX,self.positionY))
            #3 tirs par seg
        time.sleep(1.0)



