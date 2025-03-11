# GuessMu
### A propositional logic game in python

This project was done under the supervision of Balder ten Cate and Gregor Behnke at UvA, with the aim to gamify introductory logic education. Guess Mu is inspired by the classical <Guess Who?> board game; in our setting, the characters are formulas and the questions are truth assignments. 


## How to get started

1. you will need to have Python 3 installed. Add the necessary additional packages (see requirements.txt).
2. download all the .py and .png files in this repository (save everything in the same folder).
3. in settings.py you can choose the type of game you want to play.

    #### Choose the number of formulas. Options are 4, 8, 12, 16:

        N_MANY = 16

    #### Choose the maximum depth of the formulas (maximum length of a branch in its construction tree):
   
        MAX_DEPTH = 4

    #### Choose your propositional variables. Capital letters only!
       
        PROP_VARIABLES = ['P', 'Q', 'R', 'S']

    #### Choose your favourite fragment of propositional logic. Options are 'Negation', 'Conjunction', 'Disjunction', 'Conditional':
   
        CONNECTIVES = ['Negation', 'Conjunction', 'Disjunction', 'Conditional']
  
5. finally, you can run the game from guessmu.py.


## Game instructions 

1. ###  How to ask questions

In the inputbox enter the propositional variables you want to assign the value 'True' (in the game, 1) to. The rest is assumed to have gotten 'False' (in the game, 0) as value. For example, given PROP_VARIABLES as above, we have that

    pq (or p,q or qp)

all give the following assignment:

    (P, Q, R, S) = (1, 1, 0, 0)

2. ### How to deactivate/reactivate a character

Active characters have a light blue colour, and inactive ones have a dark grey. 
Left click on a character (formula) to deactivate it. 
Right click on a character to reactivate it again. 

3. ### How to remember the questions you have asked

Whenever you ask a question, the oracle's answer will be saved in the logbook. By clicking on the arrows you can scroll through your questions. 

4. ### Hint

Click and hold on the hint button to see which characters to deactivate. You can only get a hint for the latest question, so use it wisely! 

5. ### Guess Mu!

When all the characters but one have been deactivated, click on the guess button. 

6. ### Game Over 

The result of your guess will be shown on the screen. Follow the instructions. When you restart, the game will be exactly the same as before (even the secret character). See if you can finish the game in fewer steps, or why not challenge a friend to do that?!

To run a new game, close the window and rerun the program. 

7. ### Have fun!

## Suggestions

If you have any suggestions or updates for this game, I would love to hear about them!

#### Shout outs
Thank you Balder and Gregor for working with me on this project, I had a lot of fun and I learned a lot. Also, thanks to my amazing friend Laura Robinson for helping me with some design choices and drawing the funky guess logo! 
