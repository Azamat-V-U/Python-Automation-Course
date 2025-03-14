from hw_2.base import Vehicle
from hw_2.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, started, fuel, fuel_consumption, cargo, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo
        self._started = started

    def load_cargo(self, amount):
        if self.cargo + amount > self.max_cargo:
            message = "Самолет перегружен"
            raise CargoOverload(message)
        self.cargo += amount

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before
