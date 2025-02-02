from components.notifier import Notifier

def test_threshold_check():
    """Test threshold detection"""
    notifier = notifier(threshold=10)
    assert notifier.check_threshold(11) is True
    assert notifier.check_threshold(10) is False
    assert notifier.check_threshold(9.9) is False

def test_notification_message():
    """Test notification message format"""
    notifier = notifier(threshold=100)
    notifier.check_threshold(150)
    assert notifier.last_notification == "ALERT: Value 150 exceeds threshold 100!"
