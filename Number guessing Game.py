import random
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a dificulty. Type 'easy' or 'hard':: ")
computer_input = random.randint(0, 100)
print(computer_input)
attempts = 5
def user_value():
    print(f"You have {attempts} attempts remaining to guess the number")
    user_input = input("Make a guess:: ")
    ttempts -= 1




if difficulty == "easy" or difficulty == "hard":
    if difficulty == "easy":
        easy_choice()
    elif difficulty == "hard":
        hard_choice()
    
    print("Enter name is level is correct")
    # continue
else:
    print("Enter name is level is wrong")
    # break


def hard_choice():
    if user_input == computer_input():
        print("You Got it")
        
    else:
        for i in (computer_input, computer_input -25,-1):
            if user_input == i:
                print("Too Low")
                print("Guess again")
            else:
                print("Too High") 
                print("Guess again")

        





