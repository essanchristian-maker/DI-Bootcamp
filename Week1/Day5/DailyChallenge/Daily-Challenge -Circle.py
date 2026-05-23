import turtle
import math
import random

# Circle Class

class Circle:

    def __init__(self, radius):
        self.radius = radius

    # Aire
    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    # Périmètre
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    # Comparaisons
    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    # Addition — crée un nouveau cercle dont le rayon = somme des deux
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __str__(self):
        return f"Circle(radius={self.radius}, area={self.area()}, perimeter={self.perimeter()})"

    def __repr__(self):
        return f"Circle({self.radius})"


# Tests

c1 = Circle(25)
c2 = Circle(50)
c3 = Circle(15)
c4 = Circle(10)
c5 = Circle(8)

print("═" * 45)
print("CIRCLE INFO")
print("═" * 45)
print(c1)
print(c2)
print(c3)
print(c4)
print("\n" + "═" * 45)
print("COMPARISONS")
print("═" * 45)
print(f"c1 == c5 : {c1 == c5}")   # True  (both radius=5)
print(f"c1 == c2 : {c1 == c2}")   # False
print(f"c1 <  c2 : {c1 < c2}")    # True
print(f"c2 >  c3 : {c2 > c3}")    # True

print("\n" + "═" * 45)
print("ADDITION")
print("═" * 45)
c6 = c1 + c2
print(f"c1 + c2  : {c6}")         # Circle(radius=15)

print("\n" + "═" * 45)
print("SORTED")
print("═" * 45)
circles = [c1, c2, c3, c4, c5]
sorted_circles = sorted(circles)
print(f"Before : {circles}")
print(f"After  : {sorted_circles}")


# BONUS : Turtle visualisation

def draw_circles_turtle(circles):
    screen = turtle.Screen()
    screen.title("Sorted Circles")
    screen.bgcolor("black")
    screen.setup(width=900, height=500)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    colors = ["#a78bfa", "#34d399", "#f87171", "#fbbf24", "#60a5fa"]

    sorted_c = sorted(circles)
    total_width = sum(c.radius * 2 for c in sorted_c) + (len(sorted_c) + 1) * 20
    x = -total_width // 2

    for i, circle in enumerate(sorted_c):
        r     = circle.radius
        color = colors[i % len(colors)]
        cx    = x + r + 20
        cy    = -r          # centré verticalement

        # Dessine le cercle
        t.penup()
        t.goto(cx, cy)
        t.pendown()
        t.pencolor(color)
        t.fillcolor(color)
        t.begin_fill()
        t.circle(r)
        t.end_fill()

        # Label radius
        t.penup()
        t.goto(cx, cy + r + 8)
        t.pencolor("white")
        t.write(f"r={r}", align="center", font=("Arial", 10, "bold"))

        x += r * 2 + 20

    # Titre
    t.penup()
    t.goto(0, 200)
    t.pencolor("white")
    t.write("Sorted Circles (smallest → largest)",
            align="center", font=("Arial", 14, "bold"))

    screen.mainloop()


draw_circles_turtle(circles)