def get_choices():
    player_choice = input("enter your choice: ")
    if player_choice == 'rock':
        computer_choice = 'paper'
    elif player_choice == 'paper':
        computer_choice = 'scissors'
    elif player_choice == 'scissors':
        computer_choice = 'rock'

    else:
        print("invalid choice")

    decisions = {"player_choice": player_choice, "computer_choice": computer_choice}

    return decisions

choices = get_choices()
print(choices)

def user_name():
    username = input("enter your name: ")
    return username

choice_user_name = user_name()

def user_color():
    usercolor = input("enter color: ")
    return usercolor

color = user_color()

dict = {"name": choice_user_name, "color": color}
print(dict)
