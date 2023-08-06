"""
Demo for MyPy
./lib/demo_mypy.py
"""


def print_sum(num_1: int, num_2: int) -> None:
    """
    Prints sum
    """
    print(num_1 + num_2)


def get_product(num_1: int, num_2: int) -> int:
    """
    Returns product
    """
    return num_1 + num_2


A = "a"
B = "b"

print(A + B)  # Invalid format
