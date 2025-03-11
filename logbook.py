import pygame 
from pygame.locals import *
import numpy as np
from prettytable import PrettyTable


class LogBook():

    def __init__(self, x, y, width, height, backgroundcolour, framecolour, framesize, font, textcolour, gamestate):

        # log book dimensions
        self.logbook_x = x
        self.logbook_y = y 
        self.logbook_width = width 
        self.logbook_height = height 

        # background 
        self.background = pygame.Surface([width, height])
        self.background_colour = backgroundcolour
        self.background_rect = self.background.get_rect()
        self.background_rect.x = x 
        self.background_rect.y = y
        self.background.fill(self.background_colour)

        # frame
        self.frame = pygame.Rect(x, y, width, height)
        self.frame_colour = framecolour
        self.frame_size = framesize #frame thickness


        # up arrow object
        self.uparrow = pygame.image.load('uparrowsharp.png')
        self.uparrow = pygame.transform.scale_by(self.uparrow, 0.1)
        self.uparrow.convert()
        self.uparrow_rect = self.uparrow.get_rect()
        self.uparrow_rect.topright = tuple(np.subtract(self.background_rect.topright, (5, -3)))


        # down arrow object
        self.downarrow = pygame.image.load('downarrowsharp.png')
        self.downarrow = pygame.transform.scale_by(self.downarrow, 0.1)
        self.downarrow.convert()
        self.downarrow_rect = self.downarrow.get_rect()
        self.downarrow_rect.bottomright = tuple(np.subtract(self.background_rect.bottomright, (5, 3)))

        # click count
        self.click_count = 0

        # game state 
        self.gamestate = gamestate
        

        # display objects 
        self.oracle_answers = []
        
        # initial text in log book
        self.font = font
        self.text_colour = textcolour
        self.text_surface = self.font.render('', True, self.text_colour)
        self.text_center = self.text_surface.get_rect(center = self.frame.center)

        # to erase logbook
        self.erase_logbook = False



        

    def handle_event(self, event_list):

        for event in event_list: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.uparrow_rect.collidepoint(event.pos):
                    self.click_count = max(1, self.click_count - 1)
                elif self.downarrow_rect.collidepoint(event.pos):
                    self.click_count = min(len(self.oracle_answers), self.click_count + 1)
                
            if self.gamestate.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        self.erase_logbook = True




    def get_display_object(self):

        # called only when there are more questions asked than oracle answers recorded

        curr_question = self.gamestate.query_list[-1]
        curr_answer = self.gamestate.answer_list[-1]

        query_text = f'Does the secret formula \u03BC satisfy your assignment t?' 

        if curr_answer == 1:
            answer_text = f'Yes, t(\u03BC) = 1!'
        else:
            answer_text = f'No, t(\u03BC) = 0!' 

        # oracle answer to display 
    
        display_text = query_text + ' ' + answer_text

        text_surface = self.font.render(display_text, True, self.text_colour)
        text_center = text_surface.get_rect(center = tuple(np.subtract(self.frame.center, (0, 45)))) #off-center by 30

        # truthtable object to display

        truthtable_header = [''] + ['  '.join(self.gamestate.prop_vars)] + ['| \u03BC']
        truthtable_row = ['t :'] + ['   '.join(str(t) for t in curr_question)] + [f' | {curr_answer}']

        table = PrettyTable(border = False, preserve_internal_border = True)

        table.field_names = truthtable_header
        table.add_row(truthtable_row)
        table.vrules = 0

        str_tt = table.get_string() 
        str_tt = str_tt.split('\n') # length is 3

        # header

        header_surface = self.font.render(str_tt[0], True, self.text_colour)
        header_textheight = header_surface.get_height()

        header_center = header_surface.get_rect(center = tuple(np.subtract(self.frame.center, (0, -3))))

        # line 

        line_surface = self.font.render(str_tt[1], True, self.text_colour)
        line_textheight = line_surface.get_height()

        line_center = line_surface.get_rect(center = tuple(np.subtract(header_center.center, (0, -header_textheight))))

        # row 

        row_surface = self.font.render(str_tt[2], True, self.text_colour)
        row_center = row_surface.get_rect(center = tuple(np.subtract(line_center.center, (0, -line_textheight))))

        # save objects in oracle list 

        display_object = {'display text': (text_surface, text_center),
                          'tt header': (header_surface, header_center),
                          'tt line': (line_surface, line_center),
                          'tt row': (row_surface, row_center)}
        
        self.oracle_answers.append(display_object)





    def update(self):

        # update the oracle answers 

        if len(self.gamestate.query_list) > len(self.oracle_answers):
            self.get_display_object()
            self.click_count = len(self.oracle_answers) 

        # erase logbook at restart
        if self.gamestate.game_over and self.erase_logbook: 
            self.oracle_answers = []



            

    def draw(self, screen):

        # draw the input box
        screen.blit(self.background, (self.background_rect.x, self.background_rect.y))
        pygame.draw.rect(screen, self.frame_colour, self.frame, self.frame_size)

        # draw the arrows 

        screen.blit(self.uparrow, (self.uparrow_rect.x, self.uparrow_rect.y))
        # pygame.draw.rect(screen, self.frame_colour, self.uparrow_rect, self.frame_size) #for now same as frame

        screen.blit(self.downarrow, (self.downarrow_rect.x, self.downarrow_rect.y))
        # pygame.draw.rect(screen, self.frame_colour, self.downarrow_rect, self.frame_size) #for now same as frame


        # draw the text

        if len(self.oracle_answers) > 0: 

            curr_oracle_answer = self.oracle_answers[self.click_count - 1]
            # self.click_count = len(self.oracle_answers) - 1

            # blit the display text
            screen.blit(curr_oracle_answer['display text'][0], curr_oracle_answer['display text'][1])

            # blit the truth table 
            screen.blit(curr_oracle_answer['tt header'][0], curr_oracle_answer['tt header'][1])
            screen.blit(curr_oracle_answer['tt line'][0], curr_oracle_answer['tt line'][1])
            screen.blit(curr_oracle_answer['tt row'][0], curr_oracle_answer['tt row'][1])

        else: 
            ... 

