"""Main module for the hello world application."""
from typing import str

def get_greeting(name: str = "World") -> str:
    """Return a greeting message.
    
    Args:
        name: Name to greet. Defaults to "World".
    
    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"

def main() -> None:
    """Main entry point."""
    print(get_greeting())

if __name__ == "__main__":
    main()
