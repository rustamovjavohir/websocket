class Point:
    """Represents a point in 2-D space."""
    color = "None"
    x = 0
    y = 0

    def __init__(self, x, y):
        print("Constructor called")
        self.x = 0
        self.y = 0

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __del__(self):
        print(f"Destructor called {self}")


pt1 = Point(1, 2)
pt2 = Point(10, 20)

pt1.set_color("Red")
pt2.set_color("Blue")

print(pt1.__dict__)
print(pt2.__dict__)
