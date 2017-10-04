from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km

    def __str__(self):
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        return super().get_fare() + self.flagfall