Classes
    Player
        Responsibilities
            - roll die
            - hold
            - player_score

        Collaborators  
            - Game

    Computer
        Responsibilities
            - roll die until 20pts
            - hold at 20pts 
            - computer_score      

        Collaborators
            - Game

    Die
        Responsibilities
            - rolls

        Collaborators
            - Game

    Game
        Responsibilities
            - counter
            - current_player
            - round
            

            - win_condition

        Collaborators
            - Dice
            - PLayer
            - Computer


