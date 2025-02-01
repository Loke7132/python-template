def get_greeting(name: str = "World") -> str:
    """Return a greeting message.
    
    Args:
        name: Name to greet. Defaults to "World".
    
    Returns:
        A greeting string. Changed for testing in GitHub Actions.
    """
    return f"Hello, {name}!"

def main() -> None:
   
    print(get_greeting())

if __name__ == "__main__":
    main()
