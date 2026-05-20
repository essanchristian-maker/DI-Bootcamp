from datetime import date
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def display_cake(candles):
    print(f"       ___{ candles }___")
    print(f"      |:H:a:p:p:y:|")
    print(f"    __|___________|__")
    print(f"   |^^^^^^^^^^^^^^^^^|")
    print(f"   |:B:i:r:t:h:d:a:y:|")
    print(f"   |                 |")
    print(f"   ~~~~~~~~~~~~~~~~~~~")

try:
    birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")
    day, month, year = map(int, birthdate_str.split("/"))
    birthdate = date(year, month, day)
    today = date.today()

    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    candles_count = age % 10
    candles = "i" * candles_count if candles_count > 0 else "i"

    print(f"\nYou are {age} years old!\n")
    display_cake(candles)

    if is_leap_year(year):
        print("\n🎉 Bonus: You were born on a leap year! Here's a second cake!\n")
        display_cake(candles)

except ValueError:
    print("Error: please enter a valid date in DD/MM/YYYY format!")