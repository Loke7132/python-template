from src.components.calculator import calculator 

def test_calculator_add():
    calc = calculator()
    assert calc.add(2, 2) == 4

