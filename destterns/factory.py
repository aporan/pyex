#TODO: Write a short note on factory pattern

class PizzaGenerator:

    @classmethod
    def choosePizza(cls, _pizza):
        if (_pizza == "cheese"):
            pizza = CheesePizza()
        elif (_pizza == "greek"):
            pizza = GreekPizza()
        elif (_pizza == "pepperoni"):
            pizza = PepperoniPizza()
        else:
            raise("pizza type is not manufactured!")

        return pizza

class PizzaStore:

    def __init__(self, _factory):
        self.factory = _factory

    def orderPizza(self, pizza_name):

        customer_pizza = self.factory.choosePizza(pizza_name)

        customer_pizza.prepare()
        customer_pizza.bake()
        customer_pizza.cut()
        customer_pizza.box()

        return customer_pizza
        
class Pizza:

    def __init__(self): pass

    def prepare(self): print("... preparing your pizza")

    def box(self): print("... boxing ... wait to dispense")

    def cut(self): print("... slicing your pizza")

    def bake(self): print("... pizza is now baking")

# extended classses
class CheesePizza(Pizza):

    def __init__(self): super().__init__()

class GreekPizza(Pizza):

    def __init__(self): super().__init__()

class PepperoniPizza(Pizza):

    def __init__(self): super().__init__()
        
if __name__=="__main__":
    store = PizzaStore(PizzaGenerator)
    store.orderPizza("greek")
    print("Pizza dispensed. Warning: It's sizzling hot!")
