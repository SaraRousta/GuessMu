import pygame 
from gamestate import GameState
from buttons import CharacterButton
from inputbox import InputBox
from logbook import LogBook
from hintbutton import HintButton
from guessbutton import GuessButton
from gameovermenu import GameOverMenu
from globalvariables import *
from settings import *



def main():
    """ Run the game: Guess Mu! """

    # game init

    pygame.init()

    # screen 

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption('Guess Mu')


    # game state

    global_gamestate = GameState(N_MANY, MAX_DEPTH, PROP_VARIABLES, CONNECTIVES)


    # inputbox

    INPUTBOX_FONT = pygame.font.SysFont(INPUTBOX_TEXTFONT, INPUTBOX_FONTSIZE)

    inputbox = InputBox(INPUTBOX_X, INPUTBOX_Y, INPUTBOX_WIDTH, INPUTBOX_HEIGHT, INPUTBOX_BACKGROUND, INPUTBOX_FRAMECOLOUR, INPUTBOX_FRAMESIZE, INPUTBOX_FONT, INPUTBOX_TEXTCOLOUR, INPUTBOX_INITIALTEXT, INPUTBOX_CURSORWIDTH, global_gamestate)

    # logbook 

    LOGBOOK_FONT = pygame.font.SysFont(LOGBOOK_TEXTFONT, LOGBOOK_FONTSIZE)

    logbook = LogBook(LOGBOOK_X, LOGBOOK_Y, LOGBOOK_WIDTH, LOGBOOK_HEIGHT, LOGBOOK_BACKGROUND, LOGBOOK_FRAMECOLOUR, LOGBOOK_FRAMESIZE, LOGBOOK_FONT, LOGBOOK_TEXTCOLOUR, global_gamestate)

    # hint button 

    HINTBUTTON_FONT = pygame.font.SysFont(HINT_BUTTON_TEXTFONT, HINT_BUTTON_FONTSIZE)

    hintbutton = HintButton(HINT_BUTTON_X, HINT_BUTTON_Y, HINT_BUTTON_WIDTH,HINT_BUTTON_HEIGHT, HINT_BUTTON_COLOUR, HINTBUTTON_FONT, HINT_BUTTON_TEXTCOLOUR, global_gamestate)

    # guess button 

    guessbutton = GuessButton(GUESS_BUTTON_X, GUESS_BUTTON_Y, GUESS_BUTTON_WIDTH, GUESS_BUTTON_HEIGHT, GUESS_BUTTON_COLOUR, global_gamestate)

    # gameover window 

    GAMEOVER_FONT = pygame.font.SysFont(GAMEOVER_TEXTFONT, GAMEOVER_FONTSIZE, bold = True)
    GAMEOVER_FONT_GO = pygame.font.SysFont(GAMEOVER_TEXTFONT_GO, GAMEOVER_FONTSIZE_GO, bold = True)

    gameover_window = GameOverMenu(GAMEOVER_WIDTH, GAMEOVER_HEIGHT, GAMEOVER_COLOURS, (GAMEOVER_FONT, GAMEOVER_FONT_GO), GAMEOVER_TEXTCOLOUR, global_gamestate)


    # buttons and panel configuration 

    BUTTON_FONT = pygame.font.SysFont(BUTTON_TEXTFONT, BUTTON_FONTSIZE)


    characterbuttons_list = []

    for i in range(ROWS):

        x_coordinate = PANEL_X

        if i == 0: 
            y_coordinate = PANEL_Y
        else: 
            y_coordinate = y_coordinate + BUTTON_HEIGHT + V_SPACE

        for j in range(COLUMNS): 

            index = COLUMNS * i + j

            character_button = CharacterButton(BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOURS, BUTTON_FONT, BUTTON_TEXTCOLOUR, global_gamestate, index)
            
            character_button.rect.x = x_coordinate
            character_button.rect.y = y_coordinate
            character_button.text_center = character_button.name_surface.get_rect(center = character_button.rect.center)
            
            characterbuttons_list.append(character_button)

            x_coordinate = x_coordinate + BUTTON_WIDTH + H_SPACE



    # game loop

    FPS = 60
    clock = pygame.time.Clock()

    running = True

    while running: 

        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                running = False 

        # clear the screen
        screen.fill(BACKGROUND_COLOUR)



        # update events 

        for char in characterbuttons_list:
            char.update(event_list)

        inputbox.handle_event(event_list)
        inputbox.update()

        logbook.handle_event(event_list)
        logbook.update()

        hintbutton.update(event_list)
        guessbutton.update(event_list)

        gameover_window.handle_event(event_list)

        # draw on screen
        for char in characterbuttons_list:
            char.draw(screen)

        inputbox.draw(screen)
        logbook.draw(screen)
        hintbutton.draw(screen)
        guessbutton.draw(screen)
        gameover_window.draw(screen)



        # Update the screen with what we have drawn
        pygame.display.flip()
        
        # Limit to 60 frames per second
        clock.tick(FPS)

    pygame.quit()


# Call the main function, start up the game
if __name__ == "__main__":
    main()