from abc import ABC, abstractmethod

class Pizza(ABC):
    name: str = "Generic Pizza"
    toppings: list[str] = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Adding toppings:", ", ".join(self.toppings))

    def bake(self): print("Bake 25 min at 350")
    def cut(self):  print("Cutting pizza into diagonal slices")
    def box(self):  print("Place pizza in official box")
    def __str__(self): return self.name

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name="NY Style Sauce & Cheese"; self.toppings=["Reggiano cheese"]

class NYStyleVeggiePizza(Pizza):
    def __init__(self)-> None:
        self.name = 'NY Style Veggie'
        self.toppings = ['shrooms']

class NYStylePepperoniPizza(Pizza):
    def __init__(self)-> None:
        self.name = 'NY Style Pepperoni'
        self.toppings = ['Pepperoni', 'Green peppers', 'Mushrooms', 'Olive', 'Chives']

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name="Chicago Style Deep Dish Cheese"; self.toppings=["Shredded Mozzarella"]
    def cut(self): print("Cutting the pizza into square slices")

class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        self.name="Chicago Style Deep Dish Veggie"; self.toppings=["Shredded Mozzarella", 'Jalapeño', 'Shroooms']
    def cut(self): print("Cutting the pizza into star shaped slices")

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        self.name="Chicago Style Deep Dish Pepperoni"; self.toppings=["Shredded Mozzarella", 'Pepperoni', 'Oregano']
    def cut(self): print("Cutting the pizza into Michael Jordan shaped slices")