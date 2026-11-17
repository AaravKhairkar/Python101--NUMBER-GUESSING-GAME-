"""this is game.py 
    """

import random
import ui
import stats
import time
import storage

#Printing Menu
ui.show_welcome()

#Player id
player_id="Guest"

#main game
def main():

    levels = [stats.easy,stats.medium,stats.hard]

    ui.difficulty_menu(levels)

    # Selecting dificulty
    dificulty_settings = stats.chose_difficulty()

    #deffining instance attributes
    upper_limit = dificulty_settings.upper_limit
    max_attempt_limit = dificulty_settings.max_attempt_limit
    max_score = dificulty_settings.max_score
    name = dificulty_settings.name

    print(f"You Chose : Difficulty = {name}\nTotal Number Of Attempts = {max_attempt_limit}")

    # Selecting secret number
    secret = random.randint(1, upper_limit)

    # Keeping track of guesses
    user_guess_list = []
    
    # independent hints
    independent_hints = stats.Hint.get_independent_hints(secret)

    # attempts
    attempts = 0

    # starting time
    start_time = time.monotonic()

    
    # Looping until the right guess
    while True:
        
        ##guess validation
        user_guess =ui.user_choice_guess(
            upper_limit=upper_limit
            )
        
        # Repeated values 
        if user_guess in user_guess_list:
            print(f"{user_guess} - already guessed. Try another number.")
            continue

        #Guess list addition
        user_guess_list.append(user_guess)

        ##Game Logic
        attempts , guess_description = stats.game_logic(
            user_guess=user_guess,
            secret=secret,
            attempts=attempts,
            user_guess_list=user_guess_list,
        )
        
        # win condition break
        if user_guess == secret:
            break
        
        # Asking for a hint
        if attempts < max_attempt_limit:
            hint_request = input("Would you like a hint? (y/n): ")
            if hint_request.lower().strip() in ["y", "yes", "yup"]:
                # Check close/far hint first
                dependent_hints = stats.Hint.get_dependent_hint(secret, user_guess)

                stats.hint_selcetion(
                    dependent_hints=dependent_hints, 
                    independent_hints=independent_hints
                )

        ui.attempts_limit(
            attempts=attempts, 
            max_attempt_limit=max_attempt_limit
            )
        
        # max attempt limit reached
        if attempts == max_attempt_limit:
            break
    
    if user_guess == secret :        
        score = stats.score_calc(
            difficulty=dificulty_settings,
            attempts=attempts)
        win = True
    else:
        win = False
        score = 0
    
    print(f"Your Total Score is :- \n{score}")

    # time calculation
    end_time = time.monotonic()

    time_played = end_time - start_time

    minutes, seconds = divmod(time_played, 60)

    Completion_time = {"Minutes" : int(minutes),"Seconds":round(seconds,2)}

    #time played
    print(f"Completion time: {Completion_time}")

    #adding score
    attempt_data= {'Player id' : player_id,
                   'Difficulty' : name,
                   'score' : score,
                   'Win' : win,
                   'Completion time' : Completion_time 
                   }

    storage.adding_data(
        attempt_data=attempt_data
        )

#running game

main()
print()
print('*'*25)
print()

while True:
    ask = input("Wanna play Again   ")
    if ask.lower().strip() in ["y", "yes", "yup"]:
        main()
    else:
        print()
        print('*'*25)
        print()
        print("Thank You For Playing This Game")
        break


# Score & High Score Tracking
# Add descriptive attempts dictionary
