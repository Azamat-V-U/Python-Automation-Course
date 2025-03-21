import pytest
from hw_2.plane import Plane
from hw_2.exceptions import CargoOverload, LowFuelError, NotEnoughFuel


class TestPlane:
    """Набор тестов для проверки функциональности класса Plane."""

    def test_start_with_fuel(self, plane_test: Plane):
        """
        Запуск самолета с топливом.
        """
        plane_test.start()
        assert plane_test.started is True

    def test_double_start(self, plane_test: Plane):
        """
        Повторный запуск двигателя автомобиля.
        """
        plane_test.start()
        with pytest.raises(ValueError):
            plane_test.start()

    def test_start_without_fuel(self, plane_test: Plane):
        """
        Запуск самолета без топлива.
        """
        plane_test.fuel = 0
        with pytest.raises(LowFuelError):
            plane_test.start()

    def test_move_with_enough_fuel(self, plane_test: Plane):
        """
        Запуск самолета с недостаточным количеством топлива.
        """
        plane_test.start()
        distance = 500
        with pytest.raises(NotEnoughFuel):
            plane_test.move(distance)

    def test_double_move(self, plane_test: Plane):
        """
        Запуск самолета с недостаточным количеством топлива.
        """
        plane_test.start()
        distance = 250
        plane_test.move(distance)
        distance = 160
        with pytest.raises(NotEnoughFuel):
            plane_test.move(distance)

    def test_move_without_enough_fuel(self, plane_test: Plane):
        """
        Запуск самолета с недостаточным количеством топлива.
        """
        plane_test.fuel = 10.0
        plane_test.fuel_consumption = 5.0
        plane_test.start()
        with pytest.raises(NotEnoughFuel):
            plane_test.move(500)

    def test_load_cargo(self, plane_test: Plane):
        """
        Загрузка самолета грузом, не превышающий max_cargo.
        """
        amount_less = 1000
        plane_test.load_cargo(amount_less)
        assert plane_test.cargo == 1000

    def test_remove_cargo(self, plane_test: Plane):
        """
        Разгрузка самолета после загрузки
        """
        amount = 1000
        plane_test.load_cargo(amount)
        plane_test.remove_all_cargo()
        assert plane_test.cargo == 0

    def test_overload(self, plane_test: Plane):
        """
        Загрузка самолета грузом, превышающий max_cargo.
        """
        amount_more = 1001
        with pytest.raises(CargoOverload):
            plane_test.load_cargo(amount_more)
