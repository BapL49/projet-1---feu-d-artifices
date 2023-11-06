# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 22:22:25 2021

@author: antoine
"""


# -*- coding: utf-8 -*-
import pygame
import time
from pygame.locals import *
pygame.display.init()
ecran = pygame.display.set_mode((640, 480)) #Crée la fenêtre de tracé
image = pygame.image.load("./nyanCat.png") #charge une image à partir d'un fichier
ecran.blit(image, (0,0)) #Colle l'image en haut à gauche de la fenêtre de tracé (ici, l'ecran)
pygame.display.flip() #L'affichage devient effectif : l'image est rendue visible.
loop = True

Nm1 = time.monotonic()
X0 = 0

while loop: #Boucle d'événements
    if(time.monotonic()-Nm1) > 0.01:
        Nm1 = time.monotonic()
        ecran.blit(image, ((X0%500),0))
        pygame.display.flip()
        X0 = X0 + 1
    for event in pygame.event.get(): #parcours de la liste des événements
        if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #interrompt la boucle si nécessaire
            loop = False
pygame.quit()