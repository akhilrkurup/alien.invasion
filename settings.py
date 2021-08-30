# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:26:24 2021

@author: HP
"""

class Settings:
    """A class to store all Settings for Alien Invasion"""
    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        #ship settings
        self.ship_speed = 5
        self.ship_limit=3
        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width=300
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3
        #Alien settings
        self.alien_speed=1.0
        self.fleet_drop_speed = 100
        #fleet direction of 1 represents right -1 represents left
        self.fleet_direction = 1