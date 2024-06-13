# Task 4: Rock, Paper, Scissors Game with scorekeeping

# Importing the necessary libraries
from random import choice

# global variables
player_score = 0
computer_score = 0

# Defining the function to generate a random choice
def generate_choice():
        # Defining the choices
        choices = ["rock", "paper", "scissors"]
        # Generating the choice
        choice = choice(choices)
        # Returning the choice
        return choice

# Defining the function to determine the winner
def determine_winner(player_choice, computer_choice):
        # Defining the winning combinations
        winning_combinations = {
                "rock": "scissors",
                "paper": "rock",
                "scissors": "paper"
        }
        # Determining the winner
        if player_choice == computer_choice:
                return "It's a tie!"
        elif winning_combinations[player_choice] == computer_choice:
                player_score += 1
                return "You win!"
        else:
                computer_score += 1
                return "Computer wins!"

def displayscore():
        print("Player score: ", player_score)
        print("Computer score: ", computer_score)
        print("\n\n")

def main():
        # Taking the player's choice as input
        player_choice = input("Enter your choice (rock, paper, or scissors): ")
        # Generating the computer's choice
        computer_choice = generate_choice()
        # Determining the winner
        result = determine_winner(player_choice, computer_choice)
        # Printing the result
        print("Computer's choice:", computer_choice)
        print(result)

if __init__ == "__main__":
        ans = "yes"
        while ans == "yes":
                main()
                ans = input("Do you want to play again? (yes/no): ")
                displayscore()