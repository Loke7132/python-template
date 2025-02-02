from components.logger import Logger
from components.notifier import Notifier

def test_logger_notifier_integration() -> None:
    """Test notifications trigger logging."""
    logger = Logger()
    notifier = Notifier(threshold=100)
    
    result = 150
    
    if notifier.check_threshold(result):
        logger.log_operation("threshold_alert", result)
    
    assert logger.logs[-1] == "threshold_alert: 150"
