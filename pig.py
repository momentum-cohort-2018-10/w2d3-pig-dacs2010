from random import randint

class Player:
    # players:
    # roll dice
    # keep score
    def __init__(self):
        self.score = 0

    def play(self):
        '''
        player rolls die
        '''
        # take die and roll it (not sure how to implement this)
        # maybe true or false
        
        
    def hold(self):
        '''
        player chooses to keep points from rolls
        '''

# class Computer:
#     # computer (very similar to player):
#     # rolls dice
#     # keeps score
#     def __init__(self):
#         pass
#     def roll_die(self):
#         '''
#         computer rolls die until it reaches 20pts or 1 is rolled
#         '''
#         pass
#     def hold(self):
#         '''
#         computer holds when it reaches 20 pts
#         '''

#     def computer_score(self):
#         '''
#         the computers total score
#         '''
#         pass

class Die:
    def __init__(self, number):
        self.number = number
        
    def roll(self):
        '''
        return random number between 1 and 6
        '''
        return randint(1,6)

class Game:
    # game has: 
    # players 
    # rounds
    # dice
    # score
    def __init__(self):
        pass
       
        # increment by 1 every round 
        # helps choose which player is next
        self.round_counter = 0
    
    def current_player(self):
        '''
        the player who's turn it is to play
        '''
        #check round counter to toggle between players
    
    def total_score(self):
        '''
        calculates the points scored in a round and gives them to the current player
        '''
   
    def round(self):
        '''
        play one round of the game
        '''
        # pick a player to play
        # player rolls die
        # see the outcome
        # roll again? y/n
        # keep score
        # if player meets win condition game over
        # play again?