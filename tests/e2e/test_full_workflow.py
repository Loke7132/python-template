from components.calculator import Calculator
from components.logger import Logger
from components.notifier import Notifier

def test_full_workflow() -> None:
    """Test complete system workflow."""
    # Initialize components
    calc = Calculator()
    logger = Logger()
    notifier = Notifier(threshold=50)
    
    # Perform calculation
    result = calc.multiply(7, 8)  # Result is 56
    logger.log_operation("multiplication", result)
    
    # Check threshold and log alert if needed
    if notifier.check_threshold(result):
        logger.log_operation("alert", result)
    
    # Verify results
    assert result == 56
    assert logger.logs == [
        "multiplication: 56",
        "alert: 56"
    ]
