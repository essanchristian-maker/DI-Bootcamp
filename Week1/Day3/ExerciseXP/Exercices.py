#Exercice 1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1
cat1 = Cat("Chassi", 2)
cat2 = Cat("Mounina", 5)
cat3 = Cat("Choupipi", 4)

# Step 2
def find_oldest_cat(cat1, cat2, cat3):
    return max([cat1, cat2, cat3], key=lambda cat: cat.age)

# Step 3
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")


#Exercice 2

#Step 1
class Dog:
    def __init__(self, name, height):  
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")  

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2
davids_dog = Dog("George", 9)
sarahs_dog = Dog("Pika", 10)

# Step 3
for dog in [davids_dog, sarahs_dog]:
    print(f"Name: {dog.name}, Height: {dog.height} cm")
    dog.bark()
    dog.jump()
    print()

# Step 4
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same size.")



#Exercice 3

   # Create song objects
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"])


# Sing the songs
print("Stairway to Heaven:")
stairway.sing_me_a_song()



#Exercice 4

#Step 1
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, *args):
        for new_animal in args:
            if new_animal not in self.animals:
                self.animals.append(new_animal)
                print(f"{new_animal} added to {self.zoo_name}.")
            else:
                print(f"  {new_animal} is already in {self.zoo_name}.")

    def get_animals(self):
        print(f"\n Animals in {self.zoo_name}:")
        if self.animals:
            for animal in self.animals:
                print(f"  - {animal}")
        else:
            print("  (no animals yet)")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from {self.zoo_name}.")
        else:
            print(f"{animal_sold} is not in {self.zoo_name}.")

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        groups = {}
        for animal in sorted_animals:
            key = animal[0].upper()
            if key not in groups:
                groups[key] = []
            groups[key].append(animal)
        return groups

    def get_groups(self):
        groups = self.sort_animals()
        print(f"\nAnimal groups in {self.zoo_name}:")
        for letter, group in groups.items():
            print(f"{letter}: {group}")


#Step 2
zoo_of_bingerville = Zoo("ZOO OF BINGERVILLE")

#Step 3: 

# Duplicate guard
zoo_of_bingerville.add_animal("Lion")

# Display current animals
zoo_of_bingerville.get_animals()

# Sell an animal
zoo_of_bingerville.sell_animal("Bear")
zoo_of_bingerville.sell_animal("Dragon")   

# Display after sale
zoo_of_bingerville.get_animals()

# Sort and group
zoo_of_bingerville.get_groups()

#bonus *args: multiple at once
zoo_of_bingerville.add_animal("Giraffe", "Bear", "Baboon", "Lion", "Zebra")
zoo_of_bingerville.add_animal("Cat", "Cougar")