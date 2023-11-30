import pygame
import array 
from pygame import *
from pygame.locals import *
from random import random
from math import sqrt
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
                self.firework_touchee=firework
                

            if temps_actuel -self.temps_derniere_tir > self.duree_tir:#attendre 0.1 secondes entre chaque tir
                pygame.display.update(tir)

            self.temps_tir=temps_actuel
            self.temps_derniere_tir=temps_actuel

    def update_canon(self,fenetre,couleur,width,height):
        
        
        tourrelle_canon = pygame.draw.line(fenetre, couleur, (width- 95, height - 145), (width - 45, height - 110), 10)
        #tourrelle_canon = pygame.draw.line(fenetre, couleur, (width - 45, height - 110), (self.positionX+95,self.positionY+110), 10)
        pygame.display.update(tourrelle_canon)
    
    

def merge(arr, l, m, r, debut_tir):
    n1 = m - l + 1
    n2 = r - m

    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        dist_L = sqrt((L[i].positionX - debut_tir[0])**2 + (L[i].positionY - debut_tir[1])**2)
        dist_R = sqrt((R[j].positionX - debut_tir[0])**2 + (R[j].positionY - debut_tir[1])**2)

        if dist_L <= dist_R:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r, debut_tir):
    if l < r:
        m = (l + r) // 2

        mergeSort(arr, l, m, debut_tir)
        mergeSort(arr, m + 1, r, debut_tir)
        merge(arr, l, m, r, debut_tir)
