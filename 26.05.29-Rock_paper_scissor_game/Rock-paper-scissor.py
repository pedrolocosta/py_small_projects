import random

def get_choices():                                                  # creating a function for choosing options.
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):                           # creating a function to compare the options and determine the winner.
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:                                          # statement for a tied game.
        return "it's a tie!"

    elif player == "rock":                                          # statement a conditional if the player chooses rock
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rocks! You lose."

    elif player == "paper":                                         # statement a conditional if the player chooses paper
        if computer == "rock":
            return "Paper cover rock! You win!"
        else:
            return "Scissors cuts paper! You lose."

    elif player == "scissors":                                      # statement a conditional if the player chooses scissor
        if computer == "Paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

choices = get_choices()                                             # establishing player choices as a variable
result = check_win(choices["player"], choices["computer"])          # establishing the result analysis as a variable
print(result, "\n")

again = input("Do you want to play again? (y/n) ")                  # creating a cycle to continue the game

while again == "y":
    print()
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result, "\n")
    again = input("Do you want to play again? (y/n) ")

print("Thank you for playing!")
