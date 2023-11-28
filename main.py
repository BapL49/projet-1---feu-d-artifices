import pygame
from pygame import *
from pygame.locals import *
from Division import *
from Fleurs import *
from class_Tourelle import *
import math

list_fireworks = [] #liste contenant les instances de la classe division
limiteSol = 440 # position Y du sol
fenetre = display.set_mode((800,500))

turret = Tourelle(fenetre)#instance de la classe tourelle


def fireworkFunction(posY, posX): # crée les instances de la classe division
    centre_cercle = [posX, posY]
    point_n = [centre_cercle[0] - 55, centre_cercle[1]]
    for x in range(8):
        #arc tangente des points
        angle = math.atan2(point_n[1] - centre_cercle[1], point_n[0] - centre_cercle[0])
        # ajout des instances à la liste list_fireworks
        list_fireworks.append(Division(point_n[0], point_n[1], angle, fenetre))
        # calcul du nouveau point
        point_n = [(point_n[0] - posX) * math.cos(2 * math.pi / 8) - (point_n[1] - posY) * math.sin(2 * math.pi / 8) + posX, (point_n[0] - posX) * math.sin(2 * math.pi / 8) + (point_n[1] - posY) * math.cos(2 * math.pi / 8) + posY]

def gererFirework():
    for firework in list_fireworks: 
        # deltaTime in seconds.
        firework.update() # actualise la position des division
        # turret.tir((705,345),firework)
        
        current_firework=firework

        turret.tir_vers_firework((705,345),current_firework)
        # supprime la divison si elle se trouve au dessus de limiteSol
        if firework.positionY >= limiteSol or turret.collition==True:
            list_fireworks.remove(firework)



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


    debut = pygame.time.get_ticks()


    #Valeur du cercle de la tourelle
    circle_x = 755
    circle_y = 380
    circle_radius = 30 

    #Boucle d'attente avant l'apparition de la page Principale
    while pygame.time.get_ticks() - debut<5000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    #bouton pour fermer le jeu
    quit_surface=pygame.image.load("image/redx.png")
    quit_surface=pygame.transform.scale(quit_surface,(20,20))
    quit_rect = quit_surface.get_rect()

    #Boucle Continue de Jeu
    continuer = True
    while continuer :
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            # si on clique sur la croix
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if quit_rect.collidepoint(mouse_x,mouse_y):
                    continuer=False
            # si on clique dans la fenetre 
            if event.type == pygame.MOUSEBUTTONDOWN:
                # si clique gauche de la souris
                if event.button == 1:
                    if pygame.mouse.get_pos()[1] < limiteSol:
                        fireworkFunction(event.pos[1], event.pos[0])
                         


        

        fenetre.fill(BLANC)
        #Dessin du sol et de la tourelle
        sol = pygame.draw.rect(fenetre, NOIR, (0, limiteSol, 800, 20))
        tourelle_square = pygame.draw.rect(fenetre,VERT, (730, 400, 50, 50))
        tourrelle_circle = pygame.draw.circle(fenetre, VERT, (circle_x, circle_y), circle_radius )
        tourrelle_canon = pygame.draw.line(fenetre, VERT, (circle_x - 50, circle_y - 35), (circle_x, circle_y), 10)
        fenetre.blit(quit_surface,(0,0),)

        pygame.display.flip()


   
        # permet d'actualiser la position des divisions et de les supprimer
        if len(list_fireworks) > 0:
            gererFirework()
            
    
        #turret.tir_vers_souris((705,345))
        
        pygame.time.Clock().tick(30)
    pygame.quit()


main()