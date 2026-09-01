import random

user_choice = input("enter your choice: ")
computer_choice = random.choice(["rock", "paper", "scissors"])

if user_choice == computer_choice:
  tie_match = {"your choice: ": user_choice, "computer choice: ": computer_choice, "winner": "tie"}
  print(tie_match)

elif user_choice == "rock" and computer_choice == "scissors":
  response_rock = {"your choice: ": user_choice, "computer choice: ": computer_choice, "winner": "you"}
  print(response_rock)

elif user_choice == "scissors" and computer_choice == "paper":
  response_scissor = {"your choice: ": user_choice, "computer chocice: ": computer_choice, "winner": "you"}
  print(response_scissor)

elif user_choice == "paper" and computer_choice == "rock":
  response_paper = {"your choice: ": user_choice, "computer choice: ": computer_choice, "winner: ": "you"}
  print(response_paper)

else:
    response_computer = {"your choice: ": user_choice, "computer choice: ": computer_choice, "winner: ": "computer"}
    print(response_computer)
    
