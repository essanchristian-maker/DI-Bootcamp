from game import Game

# Fonction 1 : affiche le menu, retourne le choix (sans boucle)
def get_user_menu_choice():
    print("  ROCK PAPER SCISSORS")
    print("  [1] Play a new game")
    print("  [2] Show scores")
    print("  [q] Quit")
    choice = input("Select: ").strip().lower()
    return choice   # pas de boucle ici, comme demandé

# Fonction 2 : affiche le résumé des parties
# results = {"win": 2, "loss": 4, "draw": 3}
def print_results(results):
    total = sum(results.values())
    print("      GAME SUMMARY")
    print(f"   Wins  : {results['win']}")
    print(f"   Losses: {results['loss']}")
    print(f"   Draws : {results['draw']}")
    print(f"   Total : {total}")
    print("  Thanks for playing! ")

# Fonction 3 : main — boucle principale
def main():
    results = {"win": 0, "loss": 0, "draw": 0}  # dictionnaire créé ici

    while True:
        choice = get_user_menu_choice()   # affiche menu, récupère choix

        if choice == "1":
            game   = Game()               # crée un objet Game
            result = game.play()          # joue une partie, reçoit le résultat
            results[result] += 1          # mémorise le résultat

        elif choice == "2":
            print_results(results)        # affiche les scores en cours

        elif choice == "q":
            print_results(results)        # affiche le résumé final
            break

        else:
            print("Invalid option. Please choose 1, 2 or q.")

# Point d'entrée
main()