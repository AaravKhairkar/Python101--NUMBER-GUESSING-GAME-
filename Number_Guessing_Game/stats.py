#stats 

##dificulty 

from dataclasses import dataclass

@dataclass(frozen=True)
class Difficulty:
    upper_limit: int
    max_attempt_limit: int
    max_score: int
    name: str
    @property
    def points_per_attempt(self):
        points = (self.upper_limit / self.max_attempt_limit)*10
        return points
    # easy 25, medium 125, hard 1000

easy = Difficulty(upper_limit=10,max_attempt_limit=4,max_score=100,name='easy')
medium = Difficulty(upper_limit=100,max_attempt_limit=8,max_score=1000,name='medium')
hard = Difficulty(upper_limit=1000,max_attempt_limit=10,max_score=10000,name='hard')

def chose_difficulty():
    user_difficulty=input("Type difficulty  ")
    if user_difficulty.lower().strip() == "medium":
        return medium
    elif user_difficulty.lower().strip() == "hard":
        return hard
    else:
        return easy


## Game Logic   
        
def game_logic(user_guess:int,secret:int,attempts:int,user_guess_list:list):
    attempts +=1
    if user_guess == secret:
        print("Congrats!")
        print(f"It Took You {attempts} Tries")
        guess_description = 'wining guess'
    elif user_guess < secret:
        print("Too low\nTry again")
        guess_description = 'Too Low'
    elif user_guess > secret:
        print("Too high\nTry again")
        guess_description = 'Too High'
    print(f"Your Guesses:-\n{user_guess_list}")
    
    return attempts , guess_description


## Hints

# Hints class
class Hint:

    @staticmethod
    def get_dependent_hint(secret, user_guess,):##gives dependent hints based on users_guess

        diff = abs(secret - user_guess)
        if diff == 1:
            return "You're very close!"
        elif diff == 2:
            return "HOT"
        elif diff <= 5:
            return "You're close!"
        elif diff <= 8:
            return "COLD"
        elif diff <=15:
            return "You're far"
        return None

    @staticmethod
    def get_independent_hints(secret):##gives only 3 hints per round irrelevent of users guess
        hints = {}
        if secret % 2 == 0:
            hints["The Number Is Even"] = True
        else:
            hints["The Number Is Odd"] = True

        if secret % 3 == 0:
            hints["The Number Is Multiple Of 3"] = True
        else:
            hints["The Number Is Not a Multiple Of 3"] = True

        if secret % 5 == 0:
            hints["The Number Is Multiple Of 5"] = True
        else:
            hints["The Number Is Not a Multiple Of 5"] = True
        
        return hints

#Hint selecetion
def hint_selcetion(dependent_hints,independent_hints):
    if dependent_hints:
        print(dependent_hints)
    elif independent_hints:
      # Pick an available independent hint and remove it so it's not repeated
        hint_to_give = next(iter(independent_hints))
        print(hint_to_give)
        del independent_hints[hint_to_give]
    else:
        print("No more hints available!")


#calulating score
def score_calc(attempts,difficulty):
    max_attempt_limit= difficulty.max_attempt_limit
    points=difficulty.points_per_attempt

    attempts_left = max_attempt_limit - attempts + 1
    score = attempts_left * points
    return round(score)

