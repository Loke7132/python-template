from components.logger import Logger

def test_logger_initialization() -> None:
    """Test logger starts empty."""
    logger = Logger()
    assert len(logger.logs) == 0

def test_log_operation() -> None:
    """Test logging operations."""
    logger = Logger()
    logger.log_operation("add", 5)
    assert logger.logs[-1] == "add: 5"
    logger.log_operation("subtract", 3)
    assert logger.logs == ["add: 5", "subtract: 3"]
