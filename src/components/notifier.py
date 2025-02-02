class Notifier:
    def __init__(self, threshold: float):
        self.threshold = threshold
        self.last_notification = None
    
    def check_threshold(self, value: float) -> bool:
        """Check if value exceeds threshold and store notification"""
        if value > self.threshold:
            self.last_notification = f"ALERT: Value {value} exceeds threshold {self.threshold}!"
            return True
        return False
