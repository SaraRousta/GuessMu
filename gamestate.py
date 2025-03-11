from propfml import *
import random


class Character(): 

    def __init__(self, fml, truthtable):
        
        self.name = fml
        self.truthtable = truthtable
        self.alive = True


class GameState(): 

    def __init__(self, n_many, max_depth, prop_vars, connectives):

        # make the formulas
        
        self.n_many = n_many 
        self.max_depth = max_depth
        self.prop_vars = prop_vars
        self.connectives = connectives

        self.assignments = assignments(self.prop_vars)
        self.fml_list = random_n_propfml(self.n_many, self.prop_vars, self.connectives, self.max_depth, self.assignments)
        self.chars_info_list = fml_characters(self.fml_list, self.assignments)

        self.characters_list = [Character(self.chars_info_list[i][0], self.chars_info_list[i][1]) for i in range(n_many)]
        
        self.main_character_index = random.randint(0, self.n_many - 1)
        self.main_character = self.characters_list[self.main_character_index]

        # processing queries 
        
        self.query_list = []
        self.answer_list = []
        self.question_already_asked = False
        self.valid_query = True

        # flag for processing hint
        self.hint_asked = False

        # flag for restarting the game
        self.game_over = False


    def process_user_input(self, user_input):

        self.question_already_asked = False
        self.valid_query = True

        user_input = "".join(user_input.upper().split())

        if user_input == '-':
            user_input_valid = True 
        else: 
            user_input_valid = all([letter in self.prop_vars for letter in user_input])

        if user_input_valid:
            if user_input == '-':
                curr_question = tuple([0 for i in range(len(self.prop_vars))])
            else:
                curr_question = tuple([int(prop_var in user_input) for prop_var in self.prop_vars])

            if curr_question not in self.query_list:

                curr_answer = self.main_character.truthtable[curr_question]

                self.answer_list.append(curr_answer)
                self.query_list.append(curr_question)
            else:
                self.question_already_asked = True
        else:
            self.valid_query = False


    def process_hint(self, characterindex):

        character = self.characters_list[characterindex]

        if len(self.query_list) > 0:
            if character.alive:
                if character.truthtable[self.query_list[-1]] != self.answer_list[-1]:
                    return True
                else:
                    return False
            else:
                return False
        else: 
            return False


    def kill_character_helper(self):

        kill_characters_list = []

        if len(self.query_list) > 0: 
            for character in self.characters_list:
                    if character.alive:
                        if character.truthtable[self.query_list[-1]] != self.answer_list[-1]:
                            kill_characters_list.append(character)
                    else: 
                        continue

        return kill_characters_list
    
    def life_toll(self):
        alive = 0 
        for char in self.characters_list:
            if char.alive:
                alive += 1
            else:
                continue 
        
        return alive
    
    def guessed_right(self):
        
        if self.game_over:
            for i, char in enumerate(self.characters_list):
                if char.alive and i == self.main_character_index:
                    return True
                elif char.alive and i != self.main_character_index:
                    return False
                else: 
                    continue

    def restart_game(self):
                
        self.query_list = []
        self.answer_list = []
        self.question_already_asked = False
        self.valid_query = True

        self.hint_asked = False

        self.game_over = False


    def return_to_game(self):

        self.game_over = False








        