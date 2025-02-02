from src.components.calculator import Calculator
from src.components.logger import Logger
from src.components.notifier import Notifier

def test_full_workflow():
    """Test complete system workflow"""
    # Initialize components
    calc = Calculator()
    logger = Logger()
    notifier = Notifier(threshold=50)
    
    # Perform calculation
    result = calc.multiply(7, 8)  # 56
    logger.log_operation("multiplication", result)
    
    # Check threshold
    if notifier.check_threshold(result):
        logger.log_operation("alert", result)
    
    # Verify results
    assert result == 56
    assert logger.logs == [
        "multiplication: 56",
        "alert: 56"
    ]
    assert notifier.last_notification == "ALERT: Value 56 exceeds threshold 50!"
