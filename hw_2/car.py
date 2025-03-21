from hw_2.base import Vehicle
from hw_2.engine import Engine


class Car(Vehicle):
    def __init__(self, weight, started, fuel, fuel_consumption, engine: Engine):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine
        self._started = started

    def set_engine(self, engine: Engine):
        self.engine = engine
