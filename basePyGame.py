import pygame
from pygame import *
from pygame.locals import *

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

