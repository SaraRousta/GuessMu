import pygame 
from pygame.locals import *


class HintButton():
    def __init__(self, x, y, width, height, colour, textfont, textcolour, gamestate):
        """Construct a hint button"""

        # button 

        self.colour = colour 

        self.image = pygame.Surface([width, height])
        self.image.fill(self.colour)

        # get the rectangle object that has the dimension of the image
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y

        # gamestate 
        self.gamestate = gamestate 


        # text associated with this button 
        self.font = textfont 
        self.textcolour = textcolour
        self.name_surface = self.font.render("Hint", True, self.textcolour)
        self.text_center = self.name_surface.get_rect(center = self.rect.center)


    def update(self, event_list):
        for event in event_list: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos): 
                    self.gamestate.hint_asked = True
            else: 
                self.gamestate.hint_asked = False


    def draw(self, screen):
    
        # draw the button 
        self.image.fill(self.colour)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        # draw the name
        screen.blit(self.name_surface, self.text_center)