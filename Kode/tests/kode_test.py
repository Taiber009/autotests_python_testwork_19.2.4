import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2
    
    def test_subtraction_success(self):
        assert self.calc.adding(self, 3, 1) == 2
    
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1, 0)

    def test_multiply_calculate_correctly(self):
       assert self.calc.multiply(self, 2, 2) == 4
    
    def test_division_calculate_correctly(self):
       assert self.calc.multiply(self, 4, 2) == 2

    def teardown(self):
        print('Выполнение теста Teardown')
