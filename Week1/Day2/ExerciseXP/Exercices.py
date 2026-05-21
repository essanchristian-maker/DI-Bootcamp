#EXERCICE 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = dict(zip(keys, values))
print(my_dict)



#EXERCICE 2

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total = 0

for name, age in family.items():
    if age < 3:
        price = 0
        print(f"{name.capitalize()} (age {age}): Free")
    elif age <= 12:
        price = 10
        print(f"{name.capitalize()} (age {age}): $10")
    else:
        price = 15
        print(f"{name.capitalize()} (age {age}): $15")
    total += price

print(f"\nTotal cost for the family: ${total}")




#EXERCICE 3

# Create the brand dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}
#Change number_stores to 2
brand["number_stores"] = 2

#Print a sentence about Zara's clients
print(f"Zara designs clothes for: {', '.join(brand['type_of_clothes'])}.")

#Add country_creation key
brand["country_creation"] = "Spain"

#Check if international_competitors exists and add "Desigual"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

#Delete the creation_date key
brand.pop("creation_date")

#Print the last item in international_competitors
print(f"Last competitor: {brand['international_competitors'][-1]}")

#Print major colors in the US
print(f"Major colors in the US: {', '.join(brand['major_color']['US'])}")

#Print the number of keys
print(f"Number of keys in the dictionary: {len(brand)}")

#Print all keys
print(f"All keys: {list(brand.keys())}")

#BONUS 
# Create more_on_zara and merge it into brand
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 7000
}

brand.update(more_on_zara)
print("\nMerged dictionary:")
print(brand)



#EXERCICE 4

# Step 1
def describe_city(city, country="Unknown"):
    
# Step 2
    print(f"{city} is in {country}.")

# Step 3
describe_city("Reykjavik", "Iceland")   
describe_city("Paris")                 



#EXERCICE 5

# Step 1
import random

# Step 2
def compare_numbers(user_number):
    if not isinstance(user_number, int) or not (1 <= user_number <= 100):
        raise ValueError("The parameter must be an integer between 1 and 100.")

    # Step 3
    random_number = random.randint(1, 100)

    # Step 4
    if user_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

# Step 5: Call the function
compare_numbers(50)



#EXERCICE 6

# Step 1
def make_shirt(size, text):

# Step 2
    print(f"The size of the shirt is {size} and the text is {text}.")

# Step 3
make_shirt("large", "I love Python")

# Step 4: Modify with default values
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

# Step 5
make_shirt()                           
make_shirt("medium")                   
make_shirt("small", "Custom message")  

# Step 6 
make_shirt(size="small", text="Hello!")



#EXERCICE 7

import random

# Step 1
def get_random_temp():
    return random.randint(-10, 40)

# Step 2
def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")

    # Step 3
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temp < 24:
        print("Nice weather.")
    elif temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()

# Step 4 
def get_random_temp():
    return round(random.uniform(-10, 40), 1)

main()

# Step 5
def get_season(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    else:
        return "autumn"

def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10, 5), 1)
    elif season == "spring":
        return round(random.uniform(8, 20), 1)
    elif season == "summer":
        return round(random.uniform(25, 40), 1)
    else:
        return round(random.uniform(5, 18), 1)

def main():
    month = int(input("Enter a month (1-12): "))
    season = get_season(month)
    temp = get_random_temp(season)
    print(f"Season: {season.capitalize()} | Temperature: {temp}°C")

    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temp < 24:
        print("Nice weather.")
    elif temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()



#EXERCICE 8


base_price = 10
topping_price = 2.50
toppings = []

# Start the loop to collect toppings
while True:
    topping = input("Enter a topping (or 'quit' to finish): ")

    if topping == "quit":
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

print("\nYour pizza toppings:")
for t in toppings:
    print(f"  - {t}")

total = base_price + (len(toppings) * topping_price)
print(f"\nBase price:   ${base_price:.2f}")
print(f"Toppings ({len(toppings)}):  ${len(toppings) * topping_price:.2f}")
print(f"Total:        ${total:.2f}")