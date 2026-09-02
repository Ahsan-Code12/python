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

response_choice = get_choices()
print(response_choice)
