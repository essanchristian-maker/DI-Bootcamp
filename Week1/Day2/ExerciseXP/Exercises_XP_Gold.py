#EXERCICE 1

# Create the birthdays dictionary 
birthdays = {
    "Koffi":   "1995/03/15",
    "Bob":     "1997/07/22",
    "Charlie": "1994/11/08",
    "Diane":   "1998/01/30",
    "Evlyne":     "2000/06/17"
}

# Print a welcome message
print("Welcome to the Birthday Look-up! ")
print("You can look up the birthdays of the people in the list!")

# Ask the user for a name
name = input("Enter a person's name: ")

# Get the birthday from the dictionary
if name in birthdays:
    birthday = birthdays[name]
    print(f"{name}'s birthday is on {birthday}.")
else:
    print(f"Sorry, {name} is not in the list.")


    #EXERCICE 2

birthdays = {
    "Alice":   "January 14",
    "Bob":     "March 3",
    "Charlie": "July 22",
    "Diana":   "October 9",
    "Eve":     "December 31",
}

# ── Display all names ────────────────────────────────────────────────────────
print("Birthday Book")
print("─" * 30)
print("People in our records:")
for name in birthdays:
    print(f"  • {name}")
print("─" * 30)

# ── Ask for a name and look it up ────────────────────────────────────────────
person = input("\nEnter a person's name: ").strip()

if person in birthdays:
    print(f"🎉 {person}'s birthday is on {birthdays[person]}.")
else:
    print(f"Sorry, we don't have the birthday information for {person}.")


    #EXERCICE 3

    names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# ── Display available names ──────────────────────────────────────────────────
print("🎮 Character Roster:")
print("─" * 30)
for i, name in enumerate(names):
    print(f"  [{i}] {name}")
print("─" * 30)

# ── Ask for input and find index ─────────────────────────────────────────────
user_input = input("\nEnter a character name: ").strip()

if user_input in names:
    index = names.index(user_input)
    print(f"'{user_input}' was first found at index {index}.")
else:
    print(f"'{user_input}' is not in the roster.")


    #EXERCICE 4

    import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    throws = 0
    while True:
        die1 = throw_dice()
        die2 = throw_dice()
        throws += 1
        if die1 == die2:
            return throws

def main():
    results = [throw_until_doubles() for _ in range(100)]

    total   = sum(results)
    average = total / len(results)

    print(f"🎲 Results after 100 doubles:")
    print(f"   Total throws          : {total}")
    print(f"   Average throws/double : {average:.2f}")
    print(f"   Fastest double        : {min(results)} throw(s)")
    print(f"   Slowest double        : {max(results)} throw(s)")

main()


