import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return"it's a tie!"
    elif player == "rock" and computer =="scissor":
        return "Rock smashes scissors!you win!"
    elif player == "rock" and computer == "paper":
        return "Paper covers rocks! You lose."

check_win("rock", "paper")

#https://www.youtube.com/watch?v=eWRfhZUzrAc
#at 34:30 I stopped the study.