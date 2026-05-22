#Step 1,2
class Farm: 
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):

        if animal_type:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

        # Bonus Step 8: **kwargs usage → add_animal(cow=5, sheep=2)
        for animal, qty in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += qty
            else:
                self.animals[animal] = qty

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal:<10} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        # Pluralise if count > 1
        pluralised = [
            f"{a}s" if self.animals[a] > 1 else a
            for a in animal_types]
        
        # Join: "cows, goats and sheeps"
        if len(pluralised) > 1:
            animals_str = ", ".join(pluralised[:-1]) + " and " + pluralised[-1]
        else:
            animals_str = pluralised[0] if pluralised else "no animals"
        return f"{self.name}'s farm has {animals_str}."


#Standard usage 
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

#Bonus Step 8
print("\n--- Bonus: adding via **kwargs ---")
old_farm = Farm("Old MacDonald")
old_farm.add_animal(cow=3, pig=7, horse=2, chicken=14)
print(old_farm.get_info())

#Bonus
print("\n--- get_animal_types() ---")
print(old_farm.get_animal_types())

print("\n--- get_short_info() ---")
print(old_farm.get_short_info())