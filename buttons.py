import pygame 
from pygame.locals import *

class CharacterButton():

    def __init__(self, width, height, colours, textfont, textcolour, gamestate, characterindex):
        """
        Construct a button for the character
        """

        # button 
        self.alive_colour, self.dead_colour, self.help_colour = colours
        self.colour = self.alive_colour

        self.image = pygame.Surface([width, height])
        self.image.fill(self.alive_colour)

        # get the rectangle object that has the dimension of the image
        self.rect = self.image.get_rect() 

        # gamestate and character id
        self.gamestate = gamestate
        self.character_index = characterindex
        self.character = gamestate.characters_list[characterindex]

        # text associated with this button 
        self.font = textfont 
        self.textcolour = textcolour
        self.name_surface = self.font.render(self.character.name, True, self.textcolour)
        self.text_center = self.name_surface.get_rect(center = self.rect.center)


    def update(self, event_list): 
        for event in event_list: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos) and event.button == 1:
                    self.character.alive = False
                    self.colour = self.dead_colour
                if self.rect.collidepoint(event.pos) and event.button == 3: 
                    self.character.alive = True
                    self.colour = self.alive_colour

            if self.gamestate.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.colour = self.alive_colour
                     

    def draw(self, screen):
        
        # draw the button 

        if self.gamestate.hint_asked:
            if self.gamestate.process_hint(self.character_index): 
                self.image.fill(self.help_colour)
                screen.blit(self.image, (self.rect.x, self.rect.y))
            else: 
                self.image.fill(self.colour)
                screen.blit(self.image, (self.rect.x, self.rect.y))
        else: 
            self.image.fill(self.colour)
            screen.blit(self.image, (self.rect.x, self.rect.y))
        
        # draw the name
        screen.blit(self.name_surface, self.text_center)
    
