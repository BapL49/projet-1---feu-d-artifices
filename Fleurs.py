import time
import pygame


class Fleurs(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Load images for plant growth stages
        self.images = [
        pygame.image.load('image/eggplant\eggplant_1.png'),  
        pygame.image.load('image/eggplant\eggplant_2.png'),
        pygame.image.load('image/eggplant\eggplant_3.png'),
        pygame.image.load('image/eggplant\eggplant_4.png'),
        pygame.image.load('image/eggplant\eggplant_5.png'),
        pygame.image.load('image/eggplant\eggplant_6.png'),
        pygame.image.load('image/eggplant\eggplant_7.png'),
        pygame.image.load('image/eggplant\eggplant_8.png'),
        pygame.image.load('image/eggplant\eggplant_9.png'),
        ]   
        self.current_plant_stage = 0  # Variable de croissance pour chaque plante
        self.image = self.images[self.current_plant_stage]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
    def grow(self, temps_attente_secondes):
        if self.current_plant_stage < len(self.images) - 1:
            self.current_plant_stage += 1
            self.image = self.images[self.current_plant_stage]
            time.sleep(temps_attente_secondes)
    
