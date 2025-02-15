from components.calculator import Calculator

def test_calculator_add() -> None:
    """Test addition functionality."""
    calc = Calculator()
    assert calc.add(2, 2) == 4

def test_calculator_multiply() -> None:
    """Test multiplication functionality."""
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
