class Logger:
    def __init__(self):
        self.logs = []
    
    def log_operation(self, operation: str, result: float) -> None:
        self.logs.append(f"{operation}: {result}")
