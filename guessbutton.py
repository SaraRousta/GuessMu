import pygame 
from pygame.locals import *
import numpy as np


class GuessButton():
    def __init__(self, x, y, width, height, colour, gamestate):
        """Construct a guess button"""

        # button 

        self.colour = colour 

        self.image = pygame.Surface([width, height])
        self.image.fill(self.colour)

        # get the rectangle object that has the dimension of the image

        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y


        self.logo = pygame.image.load('logo.png')
        self.logo = pygame.transform.scale_by(self.logo, 0.28)
        self.logo.convert()
        self.logo_rect = self.logo.get_rect(center = self.rect.center)

        # gamestate 
        self.gamestate = gamestate 

   
    def update(self, event_list):
        for event in event_list: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos) and event.button == 1:
                    if self.gamestate.life_toll() == 1: 
                        self.gamestate.game_over = True
 


    def draw(self, screen):
    
        # draw the button 
        self.image.fill(self.colour)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        # draw the logo
        screen.blit(self.logo, (self.logo_rect.x, self.logo_rect.y))