import random

class Game:

    # Step 1 : get_user_item — boucle jusqu'à choix valide
    def get_user_item(self):
        choices = ["rock", "paper", "scissors"]
        while True:
            item = input("Choose rock, paper or scissors: ").strip().lower()
            if item in choices:
                return item
            print("Invalid choice. Please type rock, paper or scissors.")

    # Step 2 : get_computer_item — choix aléatoire
    def get_computer_item(self):
        return random.choice(["rock", "paper", "scissors"])

    # Step 3 : get_game_result — retourne win / draw / loss
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        wins = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
        if (user_item, computer_item) in wins:
            return "win"
        return "loss"

    # Step 4 : play — appelé depuis rock-paper-scissors.py
    def play(self):
        user_item     = self.get_user_item()       # 1. récupère le choix user
        computer_item = self.get_computer_item()   # 2. récupère le choix ordi
        result        = self.get_game_result(user_item, computer_item)  # 3. détermine résultat

        # Print du résultat comme demandé dans l'exercice
        messages = {
            "win" : "You win!",
            "loss": "You lose!",
            "draw": "It's a draw!"
        }
        print(f"You selected {user_item}. The computer selected {computer_item}. {messages[result]}")

        return result   # retourne "win" / "loss" / "draw"