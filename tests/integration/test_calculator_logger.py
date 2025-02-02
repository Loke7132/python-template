from components.calculator import Calculator
from components.logger import Logger

def test_calculator_logger_integration():
    """Test calculator operations are logged correctly"""
    calc = calculator()
    logger = logger()
    
    result = calc.add(5, 3)
    logger.log_operation("addition", result)
    
    result = calc.multiply(2, 4)
    logger.log_operation("multiplication", result)
    
    assert logger.logs == [
        "addition: 8",
        "multiplication: 8"
    ]
