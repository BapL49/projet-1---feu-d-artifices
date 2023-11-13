import pygame
from pygame import *
from pygame.locals import *
import time
from Division import *
import random

list_fireworks = []
fenetre = display.set_mode((800,500))

def fireworkFunction(posY, posX):
    nb_clique = 0
    nb_division = 0

    for x in range(8):
        list_fireworks.append(Division(posX, posY))



def main():

    pygame.init()

    BLANC = (255, 255, 255)
    NOIR = (0, 0, 0)
    BLEU = (0, 0, 255)
    ROUGE = (255, 0, 0)
    VERT = (0, 255, 0)

    display.set_caption("Feu d'artifice")


    mouse.set_cursor(cursors.diamond)

    fenetre_rect = fenetre.get_rect()
    image = pygame.image.load("image/Icone.jpg")
    image_rect = image.get_rect()
    image_rect.center = fenetre_rect.center
    image = pygame.transform.scale(image, (fenetre_rect.width, fenetre_rect.height))
    fenetre.blit(image, (0, 0))
    pygame.display.flip()


    debut = time.time()


    circle_x = 755
    circle_y = 380
    circle_radius = 30 


    while time.time() - debut < 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


    continuer = True
    while continuer :
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # si clique gauche de la souris
                if event.button == 1:
                    print(event.pos)
                    fireworkFunction(event.pos[1], event.pos[0])

        fenetre.fill(BLANC)
        sol = pygame.draw.rect(fenetre, NOIR, (0, 440, 800, 20))
        tourelle_square = pygame.draw.rect(fenetre,VERT, (730, 400, 50, 50))
        tourrelle_circle = pygame.draw.circle(fenetre, VERT, (circle_x, circle_y), circle_radius )
        tourrelle_canon = pygame.draw.line(fenetre, VERT, (circle_x - 50, circle_y - 35), (circle_x, circle_y), 10)

        pygame.display.flip()

        for firework in list_fireworks:
            pygame.draw.circle(fenetre, firework.couleur, (int(firework.positionX), int(firework.positionY)), firework.circle_radius)
            firework.move() 

            if firework.positionY >= 600:
                list_fireworks.remove(firework)
        
        pygame.display.flip()
        
        pygame.time.Clock().tick(30)
    pygame.quit()


main()