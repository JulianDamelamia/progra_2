import os 
print(os.getcwd())
from simple_factory.store import PizzaStore
from simple_factory.simple_factory import SimplePizzaFactory

def main():
    store = PizzaStore(SimplePizzaFactory())
    for kind in ["cheese","veggie"]:
        p = store.order_pizza(kind)
        print(f"Ordered -> {p}")

if __name__ == "__main__":
    main()
