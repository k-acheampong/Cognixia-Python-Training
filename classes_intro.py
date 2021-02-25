class Car():

    WHEELS = 4  # attribute that doesn't need to be set
    DOORS = True  # attribute that doesn't need to be set

    def __init__(self, color, make, year, HP):
        self.color = color  # attributes
        self.make = make  # attributes
        self.year = year  # attributes
        self.HP = HP  # attributes

    # method 1
    def start_car(self):
        print("Vroom")

    def remove_wheel(self):
        self.WHEELS = self.WHEELS - 1

    def __gt__(self, other):
        return self.HP > other.HP

    def __str__(self):
        return self.make


my_car = Car("red", "Tesla", 2020, 200)
your_car = Car("blue", "Ford", 2020, 100)
