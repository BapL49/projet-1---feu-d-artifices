import pygame
from pygame import *
from pygame.locals import *
import time

#Fonction Principale
def main():
    #Initialisation de pygame
    pygame.init()

    #Variable de couleur
    BLANC = (255, 255, 255)
    NOIR = (0, 0, 0)
    BLEU = (0, 0, 255)
    ROUGE = (255, 0, 0)
    VERT = (0, 255, 0)

    #Création de la fênetre en indiquant la taille et le nom
    fenetre = display.set_mode((800,500))
    display.set_caption("Feu d'artifice")

    #Changement de la forme du curseur a l'intérieur de la fênetre
    mouse.set_cursor(cursors.diamond)

    #Création de l'image de départ
    fenetre_rect = fenetre.get_rect()
    image = pygame.image.load("image/Icone.jpg")
    image_rect = image.get_rect()
    image_rect.center = fenetre_rect.center
    image = pygame.transform.scale(image, (fenetre_rect.width, fenetre_rect.height))
    fenetre.blit(image, (0, 0))
    pygame.display.flip()


    debut = time.time()


    #Valeur du cercle de la tourelle
    circle_x = 755
    circle_y = 380
    circle_radius = 30 

    #Boucle d'attente avant l'apparition de la page Principale
    while time.time() - debut < 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    #bouton pour fermer le jeu
    quit_surface=pygame.image.load("image/redx.png")
    quit_surface=pygame.transform.scale(quit_surface,(20,20))
    quit_rect = quit_surface.get_rect()

    #Boucle Continue de Jeeu
    continuer = True
    while continuer :
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if quit_rect.collidepoint(mouse_x,mouse_y):
                    continuer=False



        fenetre.fill(BLANC)
        #Dessin du sol et de la tourelle
        sol = pygame.draw.rect(fenetre, NOIR, (0, 440, 800, 20))
        tourelle_square = pygame.draw.rect(fenetre,VERT, (730, 400, 50, 50))
        tourrelle_circle = pygame.draw.circle(fenetre, VERT, (circle_x, circle_y), circle_radius )
        tourrelle_canon = pygame.draw.line(fenetre, VERT, (circle_x - 50, circle_y - 35), (circle_x, circle_y), 10)
        fenetre.blit(quit_surface,(0,0),)

        pygame.display.flip()


    pygame.quit()


main()