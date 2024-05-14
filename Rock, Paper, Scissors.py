# This program will allow you to play rock, paper, scissors against a computer.
import random

# This is where I defined my variables
options = ["Rock", "Paper", "Scissors"]

user_choice = input("Choose Rock, Paper, Scissors")


computer_choice = random.choice(options)

print("You choose: ", user_choice)
print("Computer chose: ", computer_choice)
# This is the function that will take user input and take a random input from the computer to see who wins
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("You win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You win!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("You win!")
elif user_choice == "Rock" and computer_choice == "Paper":
    print("Computer Wins!")
elif user_choice == "Scissors" and computer_choice == "Rock":
    print("Computer Wins!")
elif user_choice == "Paper" and computer_choice == "Scissors":
    print("Computer Wins!")
else:
    print("Please choose Rock, Paper, or Scissors.")
