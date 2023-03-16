import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_multiply_success(self):
        assert self.calculator.multiply(self, 2, 3) == 6

    def test_division_success(self):
        assert self.calculator.division(self, 6, 3) == 2

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 6, 3) == 3

    def test_adding_success(self):
        assert self.calculator.adding(self, 2, 3) == 5

    def teardown(self):
        print('Выполнение метода Teardown')