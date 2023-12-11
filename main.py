import pygame
from pygame import *
from pygame.locals import *
from Division import *
from Fleurs import *
from class_Tourelle import *
import math

#Initialisation de pygame
pygame.init()
info_display=pygame.display.Info() # objet contenant les informations su l'écran

HAUTEUR_FENETRE = info_display.current_h
LARGEUR_FENETRE = info_display.current_w

#Variable de couleur
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

list_fireworks = [] #liste contenant les instances de la classe division
limiteSol = HAUTEUR_FENETRE - 60 # position Y du sol
fenetre = display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE)) # initialise la fortnite

# variable de points 
global points 
points = 0

turret = Tourelle(fenetre) # instance de la classe tourelle


def fireworkFunction(posY, posX): # crée les instances de la classe division
    centre_cercle = [posX, posY]
    point_n = [centre_cercle[0] - 55, centre_cercle[1]]
    for x in range(8):
        # arc tangente des points pour calculer la direction vers laquelle se dirige la division
        angle = math.atan2(point_n[1] - centre_cercle[1], point_n[0] - centre_cercle[0])
        # ajout des instances de chaque division à la liste list_fireworks
        list_fireworks.append(Division(point_n[0], point_n[1], angle, fenetre))
        # calcul de la position du nouveau point
        point_n = [(point_n[0] - posX) * math.cos(2 * math.pi / 8) - (point_n[1] - posY) * math.sin(2 * math.pi / 8) + posX, (point_n[0] - posX) * math.sin(2 * math.pi / 8) + (point_n[1] - posY) * math.cos(2 * math.pi / 8) + posY]



def gererFirework():
    #tri fusion recursif pour trouver le firework le plus proche
    mergeSort(list_fireworks,0,len(list_fireworks)-1,debut_tir)
    for firework in list_fireworks: 
        firework.update() # actualise la position des division
        

        #methode tir 
        turret.tir_vers_firework(debut_tir,firework) # déclenche un tir vers une division du firework
        turret.update_canon(fenetre,VERT,LARGEUR_FENETRE,HAUTEUR_FENETRE) # actualise la position du canon

        
        # supprime la divison si elle se trouve au dessus de limiteSol
        if firework.positionY >= limiteSol :
            list_fireworks.remove(firework) # supprime la division concernée
            global points 
            points += 10 # ajoute 10 points à chaque division qui touche le sol
        
        # supprime la division concernée si elle est touché apr un tir de la tourelle
        if turret.collition == True and turret.firework_touchee in list_fireworks:
            list_fireworks.remove(firework)



#Fonction Principale
def main():

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
            # si clique sur la croix alors le jeu se ferme
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if quit_rect.collidepoint(mouse_x,mouse_y):
                    continuer=False
            # si on clique dans la fenetre 
            if event.type == pygame.MOUSEBUTTONDOWN:
                # si clique gauche de la souris
                if event.button == 1:
                    # initialise 8 divisions de feu d'artifice autour des coordonnées du clique
                    if pygame.mouse.get_pos()[1] < limiteSol:
                        fireworkFunction(event.pos[1], event.pos[0])
                         

        fenetre.fill(NOIR)
        
        #Dessin du sol et du cercle de la tourelle
        sol = pygame.draw.rect(fenetre, BLANC, (0, limiteSol, LARGEUR_FENETRE, 20))
        tourelle_square = pygame.draw.rect(fenetre,VERT, (LARGEUR_FENETRE - 70, HAUTEUR_FENETRE - 100, 50, 50))
        tourrelle_circle = pygame.draw.circle(fenetre, VERT, (LARGEUR_FENETRE - 45 , HAUTEUR_FENETRE - 110 ), circle_radius )
        pygame.draw.line(fenetre, VERT, (LARGEUR_FENETRE - 95, HAUTEUR_FENETRE - 145), (LARGEUR_FENETRE - 45, HAUTEUR_FENETRE - 110), 10)
        fenetre.blit(quit_surface,(0,0),)

        #position de debut du tir
        global debut_tir
        debut_tir=(LARGEUR_FENETRE - 95, HAUTEUR_FENETRE - 145)
        
        # afficher compteur de points
        font = pygame.font.SysFont('comic Sans MS', 20) # initialise la police d'écriture
        # initialisation de la position et du contenu du compteur
        compteur = font.render(f'POINTS : {points}', False, (255, 255, 255)) 
      
        # affiche le compteur
        fenetre.blit(compteur, (LARGEUR_FENETRE - 220, 30)) 
        pygame.display.flip()
   
        # permet d'actualiser la position des divisions et de les supprimer
        if len(list_fireworks) > 0:
            gererFirework()
            
        
        pygame.time.Clock().tick(30)
    pygame.quit()


main()