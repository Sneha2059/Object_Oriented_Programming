import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen

        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        ##Starting each new alien near the top left of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        # storing the alien's exact horizontal position
        self.x= float(self.rect.x)
    
     
        