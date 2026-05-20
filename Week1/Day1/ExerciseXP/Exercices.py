#EXERCICE 1

print("Hello world\n" * 4)



#EXERCICE 2

print((99**3) * 8)



#EXERCICE 3

#5 < 3                        False
#3 == 3                       True 
#3 == "3"                     False 
#"3" > 3                      Erreur 
#"Hello" == "hello"           False 
try:
    print("3" > 3)
except TypeError:
    print("TypeError: It's impossible to compare a text and a number!")
print("Hello" == "hello")  # False



#EXERCICE 4

computer_brand = "HP"
print(f"I have a {computer_brand} computer.")



#EXERCICE 5

name = "EHOUNOU"
age = 28
shoe_size = 42
info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."
print(info)



#EXERCICE 6

a = 28
b = 25
if a > b:
    print("Hello World")    




#EXERCICE 7

try:
    number = int(input("Enter a number : "))
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
except ValueError:
    print("Error: Please enter a valid number!")


#EXERCICE 8

my_name = "EHOUNOU"
user_name = input("What's your name? ")
if user_name.upper() == my_name.upper():
    print("Wait... you have the same name as me?! Are you from the EHOUNOU family? ")
else:
    print(f"Nice to meet you {user_name}! I'm {my_name}, you're definitely not in my family ")

    


#EXERCICE 9 

try:
    height = int(input("What is your height in centimeters? "))
    if height > 145:
        print("You are tall enough to ride the roller coaster!")
    else:
        print("Sorry, you need to grow some more to ride!")
except ValueError:
    print("Error: please enter a valid number!")
    