import os
import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors, you win!"
        else:
            return "Paper covers rock, you lose"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts paper, you lose."
        else:
            return "paper covers rock, you win!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors, you lose."
        else:
            return "Scissors cuts paper, you win!"
    else:
        if player != "rock" or "scissors" or "paper":
            return "You idiot, that's not a good choice, YOU ARE A LOSER!"

def game():
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)
    restart()

def restart():
    restart = input("Do you wish to play again?(y or n): ")
    if restart == "y":
        os.system("cls")
        game()
    else:
        quit()
game()

