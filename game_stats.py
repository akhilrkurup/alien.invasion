# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 20:04:57 2021

@author: HP
"""

class GameStats:
    """track statistics for alieninvasion"""
    
    def __init__(self, ai_game):
        """initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        #start alien invasion in an active state
        self.game_active=False
        with open("highscorecounter.txt") as file_object:
            contents=file_object.read()
        self.high_score=int(contents)
        
    def reset_stats(self):
        """initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score=0
        self.level=1
        
        