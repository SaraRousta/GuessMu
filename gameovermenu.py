import pygame 
import numpy as np

class GameOverMenu():

    def __init__(self, width, height, colours, fonts, textcolour, gamestate):
        
        self.colour_correct, self.colour_incorrect = colours
        self.image = pygame.Surface([width, height])

        self.gamestate = gamestate 
        
        self.font, self.fontgo = fonts
        self.text_colour = textcolour
        

    def handle_event(self, event_list):
        
        for event in event_list:
            if self.gamestate.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.gamestate.restart_game()
                elif event.key == pygame.K_ESCAPE: 
                    self.gamestate.return_to_game()

    def draw(self, screen):

        if self.gamestate.guessed_right() == True:

            # game over window
  
            gameover_window = self.image.get_rect(center = screen.get_rect().center)
            self.image.fill(self.colour_correct)

            screen.blit(self.image, gameover_window)

            # correct guess
            
            text_surface = self.font.render('Congrats, you guessed \u03BC!', True, self.text_colour)
            text_height = text_surface.get_height()

            text_center = text_surface.get_rect(center = tuple(np.subtract(gameover_window.center, (0, 40))))

            screen.blit(text_surface, text_center)

            # score

            score_surface = self.fontgo.render(f'You did it with {len(self.gamestate.query_list)} questions.', True, self.text_colour)
            score_height = score_surface.get_height()

            score_center = score_surface.get_rect(center = tuple(np.subtract(text_center.center, (0, -int(text_height*2)))))

            screen.blit(score_surface, score_center)

            # steps

            steps_surface = self.fontgo.render('Want to try to get it in fewer steps?', True, self.text_colour)
            steps_height = steps_surface.get_height()

            steps_center = steps_surface.get_rect(center = tuple(np.subtract(score_center.center, (0, -score_height))))

            screen.blit(steps_surface, steps_center)

            # restart             
            
            restart_surface = self.fontgo.render('Press space to play again.', True, self.text_colour)
            restart_height = restart_surface.get_height()

            restart_center = restart_surface.get_rect(center = tuple(np.subtract(steps_center.center, (0, -steps_height))))

            screen.blit(restart_surface, restart_center)

            # return to game            
            
            continue_surface = self.fontgo.render('Press escape to return to game.', True, self.text_colour)

            continue_center = continue_surface.get_rect(center = tuple(np.subtract(restart_center.center, (0, -restart_height))))

            screen.blit(continue_surface, continue_center)


        elif self.gamestate.guessed_right() == False:
            
            # game over window
  
            gameover_window = self.image.get_rect(center = screen.get_rect().center)
            self.image.fill(self.colour_incorrect)

            screen.blit(self.image, gameover_window)

            # incorrect guess 

            text_surface = self.font.render('That was not \u03BC!', True, self.text_colour)
            text_height = text_surface.get_height()

            text_center = text_surface.get_rect(center = tuple(np.subtract(gameover_window.center, (0, 40))))

            screen.blit(text_surface, text_center)


            # continue              
            
            continue_surface = self.fontgo.render('Press escape to return to game and continue.', True, self.text_colour)
            continue_height = continue_surface.get_height()

            continue_center = continue_surface.get_rect(center = tuple(np.subtract(text_center.center, (0, -text_height*3))))

            screen.blit(continue_surface, continue_center)

            # restart             
            
            restart_surface = self.fontgo.render('Press space to restart and try again.', True, self.text_colour)
            restart_center = restart_surface.get_rect(center = tuple(np.subtract(continue_center.center, (0, -continue_height))))

            screen.blit(restart_surface, restart_center)












