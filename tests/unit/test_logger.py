from components.logger import Logger

def test_logger_initialization():
    """Test logger starts empty"""
    logger = logger()
    assert len(logger.logs) == 0

def test_log_operation():
    """Test logging operations"""
    logger = logger()
    logger.log_operation("add", 5)
    assert logger.logs[-1] == "add: 5"
    logger.log_operation("subtract", 3)
    assert logger.logs == ["add: 5", "subtract: 3"]
