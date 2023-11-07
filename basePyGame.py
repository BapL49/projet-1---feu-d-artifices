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

while time.time() - debut < 5:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

continuer = True
while continuer :
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False


    mouse_x, mouse_y = mouse.get_pos()
    circle_x, circle_y = mouse_x, mouse_y

    fenetre.fill(BLANC)
    tourrelle_circle = draw.circle(fenetre, VERT, (circle_x, circle_y), circle_radius )
    print(mouse_x, mouse_y)

    pygame.display.flip()


pygame.quit()