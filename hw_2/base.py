from abc import ABC
from hw_2.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self._started = False
        self._fuel = fuel
        self.fuel_consumption = fuel_consumption

    @property
    def started(self):
        return self._started

    @started.setter
    def started(self, value):
        self._started = value

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, value):
        self._fuel = value

    def start(self):
        if not self._started:
            if self.fuel > 0:
                self._started = True
            else:
                message = "Недостаточно топлива для запуска"
                raise LowFuelError(message)
        else:
            message = "Двигатель уже запущен"
            raise ValueError(message)

    def move(self, distance):
        required_fuel = distance * (self.fuel_consumption / 100)
        if not self._started:
            message = "Двигатель не запущен"
            raise ValueError(message)
        elif required_fuel > self.fuel:
            message = "Недостаточно топлива для передвижения"
            raise NotEnoughFuel(message)
        self.fuel -= required_fuel
