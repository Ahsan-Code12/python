import random

user_choice = input("enter your choice: ")
computer_choice = random.choice(["rock", "paper", "scissors"])

if user_choice == computer_choice:
  tie_match = {"your choice: ": user_choice, "computer choice: ": computer_choice, "winner": "tie"}
  print(tie_match)

elif user_choice == "rock" and computer_choice == "scissors":
  rockwin = {"your choice: ": user_choice, "computer choice: ": computer_choice, "winner": "you"}
  print(rockwin)

elif user_choice == "scissors" and computer_choice == "paper":
  sciss_win = {"your choice: ": user_choice, "computer chocice: ": computer_choice, "winner": "you"}
  print(sciss_win)

elif user_choice == "paper" and computer_choice == "rock":
  paper_win = {"your choice: ": user_choice, "computer choice: ": computer_choice, "winner: ": "you"}
  print(paper_win)

else:
    computer_wins = {"your choice: ": user_choice, "computer choice: ": computer_choice, "winner: ": "computer"}
    print(computer_wins)
    
