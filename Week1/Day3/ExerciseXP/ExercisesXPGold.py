#EXERCICE 1

import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def definition(self):
        print(
            "A circle is a perfectly round 2D shape where every point\n"
            f"on its boundary is exactly {self.radius} unit(s) away from\n"
            "its center — that fixed distance is called the radius."
        )


# ── Test with default radius ────────────────────────────────────────────────
c1 = Circle()
print("=== Circle (default radius = 1.0) ===")
c1.definition()
print(f"Perimeter : {c1.perimeter():.4f}")
print(f"Area      : {c1.area():.4f}")

# ── Test with a custom radius ────────────────────────────────────────────────
print("\n=== Circle (radius = 7) ===")
c2 = Circle(7)
c2.definition()
print(f"Perimeter : {c2.perimeter():.4f}")
print(f"Area      : {c2.area():.4f}")


#EXERCICE 2

import random

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reverse(self):
        return self.letters[::-1]

    def sort(self):
        return sorted(self.letters)

    def generate_random(self):
        return [random.randint(1, 100) for _ in self.letters]


# ── Test ────────────────────────────────────────────────────────────────────
my_list = MyList(['d', 'a', 'c', 'b', 'e', 'f'])

print(f"Original : {my_list.letters}")
print(f"Reversed : {my_list.reverse()}")
print(f"Sorted   : {my_list.sort()}")
print(f"Random   : {my_list.generate_random()}")



#EXERCICE 3

class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup",              "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger",         "price": 15, "spice": "A", "gluten": True },
            {"name": "Salad",             "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries",      "price":  5, "spice": "C", "gluten": False},
            {"name": "Beef Bourguignon",  "price": 25, "spice": "B", "gluten": True },
        ]

    # ── Helper: find a dish by name (case-insensitive) ──────────────────────
    def _find(self, name):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                return dish
        return None

    # ── Helper: display the full menu ───────────────────────────────────────
    def display_menu(self):
        spice_label = {"A": "Not spicy", "B": "A little spicy", "C": "Very spicy"}
        print(f"\n{'─'*55}")
        print(f"  {'DISH':<22} {'PRICE':>6}  {'SPICE':<16} {'GLUTEN'}")
        print(f"{'─'*55}")
        for dish in self.menu:
            gluten = "✅ Yes" if dish["gluten"] else "❌ No"
            spice  = spice_label[dish["spice"]]
            print(f"  {dish['name']:<22} ${dish['price']:>5}  {spice:<16} {gluten}")
        print(f"{'─'*55}\n")

    # ── Add ─────────────────────────────────────────────────────────────────
    def add_item(self, name, price, spice, gluten):
        if self._find(name):
            print(f"⚠️  '{name}' is already on the menu. Use update_item() to modify it.")
            return
        self.menu.append({"name": name, "price": price, "spice": spice, "gluten": gluten})
        print(f"✅ '{name}' has been added to the menu.")

    # ── Update ──────────────────────────────────────────────────────────────
    def update_item(self, name, price, spice, gluten):
        dish = self._find(name)
        if not dish:
            print(f"❌ '{name}' is not on the menu.")
            return
        dish["price"] = price
        dish["spice"] = spice
        dish["gluten"] = gluten
        print(f"✏️  '{name}' has been updated.")

    # ── Remove ──────────────────────────────────────────────────────────────
    def remove_item(self, name):
        dish = self._find(name)
        if not dish:
            print(f"❌ '{name}' is not on the menu.")
            return
        self.menu.remove(dish)
        print(f"🗑️  '{name}' has been removed from the menu.")


# ── Test ─────────────────────────────────────────────────────────────────────
manager = MenuManager()

print("=== Initial Menu ===")
manager.display_menu()

print("=== Add Items ===")
manager.add_item("Pasta", 14, "A", True)
manager.add_item("Soup", 10, "B", False)    # duplicate guard
manager.display_menu()

print("=== Update Item ===")
manager.update_item("Salad", 20, "A", False)     # price bump
manager.update_item("Sushi", 22, "A", False)     # not found
manager.display_menu()

print("=== Remove Item ===")
manager.remove_item("French Fries")
manager.remove_item("Pizza")                     # not found
manager.display_menu()