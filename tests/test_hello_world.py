from hello_world.main import get_greeting

def test_greeting() -> None:
    """Test the greeting function."""
    assert get_greeting() == "Hello, World!"
    assert get_greeting("Test") == "Hello, Test!"

def test_basic_math() -> None:
    """Basic test"""
    assert 2 + 2 == 4
