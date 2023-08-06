# ./lib/demo_mypy.py
def print_sum(x: int, y: int) -> int:  # Should return None
    print(x + y)


def get_product(x: int, y: int) -> str:  # Should return int
    return x + y

a = "a"
b = "b"

print(a * b) # Invalid format