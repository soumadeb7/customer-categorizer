from pathlib import Path

def from_root(*paths):
    """
    Returns an absolute path inside the project root.
    Usage:
        from_root('src', 'logger') -> C:/Desktop/Customer-Categorizer/src/logger
    """
    return Path(__file__).parent.resolve().joinpath(*paths)
