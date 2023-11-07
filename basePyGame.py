import pygame
from pygame import *
from pygame.locals import *
import time


pygame.init()

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

fenetre = display.set_mode((800,500))
display.set_caption("Feu d'artifice")

circle_radius = 30 

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
circle_y = 410
circle_radius = 30 

angle = 45

sol = pygame.draw.rect(fenetre, NOIR, (0, 480, 800, 20))
tourelle_square = pygame.draw.rect(fenetre,VERT, (730, 430, 50, 50))
tourrelle_circle = pygame.draw.circle(fenetre, VERT, (circle_x, circle_y), circle_radius )



while time.time() - debut < 5:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


continuer = True
while continuer :
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

    fenetre.fill(BLANC)
    sol = pygame.draw.rect(fenetre, NOIR, (0, 480, 800, 20))
    tourelle_square = pygame.draw.rect(fenetre,VERT, (730, 430, 50, 50))
    tourrelle_circle = pygame.draw.circle(fenetre, VERT, (circle_x, circle_y), circle_radius )

    pygame.display.flip()


pygame.quit()