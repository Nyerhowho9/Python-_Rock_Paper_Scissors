import random
game_choices = ["R", "P", "S"]

def computer_selection():
    computer_choice = random.choice(game_choices)
    return computer_choice

def user_selection():
    user_choice = input("Select your weapon: R, P or S \n" )
    capitalized_user_choice = user_choice.capitalize()
    return capitalized_user_choice

def invalid_user_selection():
    
    if user_selection() not in game_choices:
        print("Error!! Your selection is invalid. Try again")
        user_selection() 
        game_play()   

def game_play():
    if user_selection() == "R":
        if computer_selection() == "P":
            print("Computer wins!!! You lose")
        elif computer_selection() == "S":
            print("You win!!! Computer loses")
        elif computer_selection() == "R":
            print("It's a tie. Try a second round") 
            user_selection()  

    elif user_selection() == "P":
        if computer_selection() == "P":
            print("It's a tie. Try a second round") 
            user_selection() 
        elif computer_selection() == "S":
            print("Computer wins!!! You lose")
        elif computer_selection() == "R":
            print("You win!!! Computer loses")
    elif user_selection() == "S":
        if computer_selection() == "P":
            print("You win!!! Computer loses") 
        elif computer_selection() == "S":
            print("It's a tie. Try a second round") 
            user_selection()
        elif computer_selection() == "R":
            print("Computer wins!!! You lose")
    else:
        invalid_user_selection()        
game_play()



