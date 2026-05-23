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