import pygame
from pygame.locals import *
import time

class InputBox():

    def __init__(self, x, y, width, height, boxcolour, framecolour, framesize, font, textcolour, initialtext, cursorwidth, gamestate):
        """
        Construct an input box. 
        """

        # initial text in input box
        self.font = font
        self.text_colour = textcolour
        self.initaltext = initialtext
        self.text = initialtext
        self.text_surface = self.font.render(self.text, True, textcolour)
        
        # size and colour of the input box:

        # background 
        self.box = pygame.Surface([max(self.text_surface.get_width() + 10, width), height])
        self.box_colour = boxcolour
        self.box_rect = self.box.get_rect()
        self.box_rect.x = x 
        self.box_rect.y = y
        self.box.fill(self.box_colour)

        # frame
        self.frame = pygame.Rect(x, y, max(self.text_surface.get_width() + 10, width), height)
        self.frame_colour = framecolour
        self.frame_size = framesize
    
        # add a cursor 
        self.cursor_width = cursorwidth
        self.text_rect = self.text_surface.get_rect(topleft = (self.frame.x + 9, self.frame.y + 9))
        self.cursor = pygame.Rect(self.text_rect.midright, (self.cursor_width, self.text_rect.height + 2))

        # widest character 
        self.W_width = font.render('W', True, self.text_colour).get_width()

        # clicked 
        self.active = False

        # gamestate 
        self.gamestate = gamestate 
        

    
    def handle_event(self, event_list):

        for event in event_list: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.frame.collidepoint(event.pos):
                    if self.text == self.initaltext: 
                        self.text = ''
                    self.active = True
                else: 
                    self.active = False
                
                # self.colour = TEXTBOX_COLOUR_ACTIVE if self.active else TEXTBOX_COLOUR_INACTIVE


            if self.active and event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RETURN: 
                    self.gamestate.process_user_input(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                    # disallow the characters to exceed the border
                    if self.text_surface.get_width() > self.frame.w - self.W_width:
                        self.text = self.text[:-1]

                
    def update(self):

        # render the text again 
        self.text_surface = self.font.render(self.text, True, self.text_colour)
        
        # update the cursor position
        self.text_rect.size = self.text_surface.get_size()
        self.cursor.midleft = self.text_rect.midright


    def draw(self, screen):

        # draw the input box
        screen.blit(self.box, (self.box_rect.x, self.box_rect.y))
        pygame.draw.rect(screen, self.frame_colour, self.frame, self.frame_size)

        # show the text inside the input box
        screen.blit(self.text_surface, (self.frame.x + 9, self.frame.y + 9))
        
        # cursor is made to blink after every 0.5 sec
        if time.time() % 1 > 0.5 and self.active:
            pygame.draw.rect(screen, self.frame_colour, self.cursor)