"""A stub for a library module"""

from logging import NullHandler, getLogger

logger = getLogger(__name__).addHandler(NullHandler())


def hello_world() -> str:
    """
    A placeholder function that returns a value.

    Returns:
        Hello World!
    """
    return "Hello World!"
