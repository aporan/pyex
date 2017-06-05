#!/usr/bin/env python3
# TODO: Write short note on decorator pattern

class BasicCar(object):

    def __init__(self): pass
    def assemble(self): print("Basic Car.")

class CarDecorator(object):

    def __init__(self, car_instance):  self.car = car_instance
    def assemble(self): self.car.assemble()

class SportsCar(CarDecorator):

    def __init__(self, car_instance): super().__init__(car_instance)

    def assemble(self):
        super().assemble()
        print(" Adding features of Sports Car.")

class LuxuryCar(CarDecorator):

    def __init__(self, car_instance): super().__init__(car_instance)

    def assemble(self):
        super().assemble()
        print(" Adding features of Luxury Car.")

if __name__ == "__main__":
    sports_car = SportsCar(BasicCar())
    sports_car.assemble()

    print("\n**********")

    sports_luxury_car = SportsCar(LuxuryCar(BasicCar()))
    sports_luxury_car.assemble()
    
