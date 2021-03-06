from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        breakdown_chance = random.randint(0, 100)
        if breakdown_chance > self.reliability:
            return 0
        return super().drive(distance)
