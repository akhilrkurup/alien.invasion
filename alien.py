# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 19:47:24 2021

@author: HP

"""

import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    
    def __init__(self, ai_game):
        """Initialize the alien and set it's starting position"""
        super().__init__()
        self.screen=ai_game.screen
        
        #Load the alien and set it's rect attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
            
        #Start each new alien near the top left of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #store the alien's exact horizontal position
        self.x = float(self.rect.x)
        self.settings=ai_game.settings
        
    def update(self):
       """"Move the alien to the right or left"""
       self.x += self.settings.alien_speed*self.settings.fleet_direction
       self.rect.x = self.x
    def check_edges(self):
        """ return true if the alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True