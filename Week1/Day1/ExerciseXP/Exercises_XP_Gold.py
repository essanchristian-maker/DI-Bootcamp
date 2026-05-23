#Exercice 1 

month = int(input("Enter a month (1-12): "))

if month < 1 or month > 12:
    print("Invalid input. Please enter a number between 1 and 12.")
elif month in [3, 4, 5]:
    print("Spring ")
elif month in [6, 7, 8]:
    print("Summer ")
elif month in [9, 10, 11]:
    print("Autumn ")
else:                          
    print("Winter ")


#Exercice 2

#First
for i in range(1, 21):
    print(i)
#Second 
for index, value in enumerate(range(1, 21)):
    if index % 2 == 0:
        print(f"index {index} → {value}")




#Exercice 3

MY_NAME = "Christian"

name = input("Enter a name: ").strip()

while name.lower() != MY_NAME.lower():
    print(f"'{name}' is not the right name. Try again!")
    name = input("Enter a name: ").strip()

print(f"Welcome, {name}! ")


#Exercice 4

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name = input("Enter a name: ").strip()

names_lower = [n.lower() for n in names]

if name.lower() in names_lower:
    index = names_lower.index(name.lower())
    print(f"'{names[index]}' first appears at index {index}.")
else:
    print(f"'{name}' is not in the list.")



#Exercice 5

numbers = []

for i, label in enumerate(["1st", "2nd", "3rd"], start=1):
    n = float(input(f"Input the {label} number: "))
    numbers.append(n)

print(f"The greatest number is: {max(numbers)}")



#Exercice 6

import random

wins   = 0
losses = 0

while True:
    secret = random.randint(1, 9)
    
    while True:
        try:
            guess = int(input("\nGuess a number (1-9): "))
            if 1 <= guess <= 9:
                break
            print("Please enter a number between 1 and 9.")
        except ValueError:
            print(" Invalid input. Enter a whole number.")
    
    if guess == secret:
        print("Winner!")
        wins += 1
    else:
        print(f"Better luck next time! The number was {secret}.")
        losses += 1
    
    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        break

total = wins + losses
print(f"""
    GAME OVER

  Wins   : {wins}
  Losses : {losses}
   Total  : {total}
  Rate   : {wins/total*100:.1f}%
""")