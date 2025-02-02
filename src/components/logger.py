class Logger:
    def __init__(self) -> None:
        self.logs: list[str] = []  # Explicitly typed as a list of strings
    
    def log_operation(self, operation: str, result: float) -> None:
        """Log an operation with its result."""
        self.logs.append(f"{operation}: {result}")
