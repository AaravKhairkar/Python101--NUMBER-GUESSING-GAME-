"""ui.py - display and input only. No game rules live here."""


##menu 
def show_welcome():
    print("WELCOME TO")
    print("GUESS : THE NUMBER GAME")
    print("Try to guess a number between the Range of Your Choice")

def difficulty_menu(difficulty):
    print()
    for number, d in enumerate(difficulty, start=1):
        print(f"{number}. {d.name}:- 1 to {d.upper_limit}")
    print()

# Error Class
class CustomValueError(Exception):
    pass

## Guessed number and its validation validation

def user_choice_guess(upper_limit,CustomValueError=CustomValueError):
    while True:
        try:
            user_input = input("Enter Your Guess: ")
            try:
                val = int(user_input)
            except ValueError:
                raise CustomValueError("Type Error: Please enter a valid integer.")
            if val not in range(1,upper_limit+1):
                raise CustomValueError(f"Inbound Value Error: Number must be between 1 and {upper_limit}")
            return val
        except CustomValueError as e:
            print(f"Plz Enter A Valid Number\nYour error: {e}")
            continue

#attempts calculation
def attempts_limit(attempts,max_attempt_limit):
    print(f"Attempts :-  {attempts}")
    if attempts >= max_attempt_limit :
        print("You Ran Out Of Attempts")
    else:
        print(f"Remaining Attempts = {(max_attempt_limit - attempts)}")

