import random
from colorama import init, Fore

init(autoreset=True)

winning_combinations = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def display_choices():
    print(Fore.YELLOW + "\nRock Paper Scissors")
    print(Fore.CYAN + "1. Rock")
    print(Fore.CYAN + "2. Paper")
    print(Fore.CYAN + "3. Scissors")

def player_choice():
    while True:
        choice = input(Fore.GREEN + "Choose Rock, Paper or Scissors: ").lower()

        if choice in ["rock", "paper", "scissors"]:
            return choice

        print(Fore.RED + "Invalid Choice")

def ai_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def check_winner(player, ai):
    if player == ai:
        return "draw"
    elif winning_combinations[player] == ai:
        return "player"
    else:
        return "ai"

def display_result(player, ai, result):
    print()
    print(Fore.MAGENTA + "Player: " + player)
    print(Fore.BLUE + "AI: " + ai)

    if result == "player":
        print(Fore.GREEN + "Player Wins!")
    elif result == "ai":
        print(Fore.RED + "AI Wins!")
    else:
        print(Fore.YELLOW + "It's a Draw!")

def main():
    print(Fore.YELLOW + "Welcome to Rock Paper Scissors!")

    while True:
        display_choices()

        player = player_choice()
        ai = ai_choice()

        result = check_winner(player, ai)

        display_result(player, ai, result)

        again = input(Fore.GREEN + "\nPlay again? (yes/no): ").lower()

        if again != "yes":
            print(Fore.YELLOW + "Thanks for playing!")
            break

if __name__ == "__main__":
    main()