import random

user_choice = input("enter your choice: ")
computer_choice = random.choice(["rock", "paper", "scissors"])

if computer_choice == user_choice:
    tie = {"user": user_choice, "computer": computer_choice, "tie": True}
    print(tie)
elif computer_choice == "rock" and user_choice == "paper":
    userwin = {"computer choice": computer_choice, "user choice": user_choice, "winner": "user"}
    print(userwin)
elif computer_choice == "paper" and user_choice == "scissors":
    scissorwin = {"computer choice": computer_choice, "user choice": user_choice, "winner": "user"}
    print(scissorwin)
elif computer_choice == "scissors" and user_choice == "rock":
    rockwin = {"computer choice": computer_choice, "user choice": user_choice, "winner": "user"}
    print(rockwin)
else:
    computer_win = {"computer choice": computer_choice, "user choice": user_choice, "winner": "computer"}
    print(computer_win)
