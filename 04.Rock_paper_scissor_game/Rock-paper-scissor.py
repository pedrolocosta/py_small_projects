import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return"it's a tie!"
    elif player == "rock":
        if computer =="scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rocks! You lose."
    elif player == "Paper":
        if computer == "rock":
            return "Paper cover rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
