#Exercice 1 : Pets

#Classes 

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#Step 1

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#Step 2
bengal_obj    = Bengal("Safir", 3)
chartreux_obj = Chartreux("Nouna", 4)
siamese_obj   = Siamese("Biby", 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

#Step 3

sara_pets = Pets(all_cats)

#Step 4

sara_pets.walk()



#Exercice 2 :Dog 

#Step 1
class Dog:
    def __init__(self, name, age, weight):
        self.name   = name
        self.age    = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power    = self.run_speed()    * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} wins the fight!"
        elif other_power > my_power:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a draw!"

#Step 2 

dog1 = Dog("Roliff",   5, 30)
dog2 = Dog("Vogrer", 3, 20)
dog3 = Dog("Fitim",  4, 35)

#Step 3

print(dog1.bark())           # bark()
print(dog2.bark())
print(dog3.bark())

print(dog1.run_speed())      # run_speed()
print(dog2.run_speed())
print(dog3.run_speed())

print(dog1.fight(dog2))      # fight()
print(dog2.fight(dog3))
print(dog1.fight(dog3))


#Exercice 3

# Step 1 : imports

import random
from Exercice2 import Dog                        

#Step 2 : Classe PetDog 

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight) 
        self.trained = False                

    def train(self):
        print(self.bark())                 
        self.trained = True

    def play(self, *args):                  
        names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet!")

#Step 3

dog1 = PetDog("Fido",  2, 10)
dog2 = PetDog("Buddy", 3, 15)
dog3 = PetDog("Max",   4, 20)

# train()
print("train()")
dog1.train()
print(f"dog1.trained = {dog1.trained}")

# play()
print("\n play() ")
dog1.play(dog2, dog3)

# do_a_trick() 
print("\n do_a_trick() sans training ")
dog2.do_a_trick()

# do_a_trick() 
print("\n do_a_trick() après training")
dog2.train()
dog2.do_a_trick()
dog2.do_a_trick()  


#Exercice 4 

#Step 1

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age        = age
        self.last_name  = ""             
    def is_18(self):
        return self.age >= 18
    
#Step 2 
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members   = []               

    def born(self, first_name, age):
        person           = Person(first_name, age)
        person.last_name = self.last_name 
        self.members.append(person)
        print(f"Welcome to the family, {first_name} {self.last_name}! ")

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John "
                          f"accept that you will go out with your friends.")
                else:
                    print(f"Sorry {first_name}, "
                          f"you are not allowed to go out with your friends.")
                return                   
        print(f" {first_name} is not a member of the {self.last_name} family.")

    def family_presentation(self):
        print(f"\n The {self.last_name} Family")
        print("─" * 30)
        for member in self.members:
            status = "adult" if member.is_18() else "minor"
            print(f"  • {member.first_name:<12} age: {member.age:<4} {status}")
        print("─" * 30)


#Tests

family = Family("Johnson")

family.born("Jane",  45)
family.born("John",  47)
family.born("Sarah", 17)
family.born("Tom",   20)
family.born("Lily",   8)

print()
family.check_majority("Tom")
family.check_majority("Sarah")
family.check_majority("Lily")
family.check_majority("Kevin")  

family.family_presentation()