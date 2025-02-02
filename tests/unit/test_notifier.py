from components.notifier import Notifier

def test_threshold_check() -> None:
    """Test threshold detection."""
    notifier = Notifier(threshold=10)
    assert notifier.check_threshold(11) is True
    assert notifier.check_threshold(10) is False
    assert notifier.check_threshold(9.9) is False
