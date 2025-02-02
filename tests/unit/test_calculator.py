from src.components.calculator import Calculator 

def test_calculator_add():
    calc = Calculator()
    assert calc.add(2, 2) == 4

