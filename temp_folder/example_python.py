"""demo module to practice git."""


def add_numbers(a, b):
    """Return the addition of the given numbers."""
    return sum(a, b)


# 1. extend add_numbers to allow any arbitrary number of parameters.
# 2. Investigate security exploit of add numbers
# 3. Make it more performant
# 4. Add documentation


def average_of_numbers(a, b):
    """Return the average of the given two numbers."""
    return sum(a, b) / 2


def multiply_numbers(a, b):
    """Return the multiplication of two numbers."""
    result = a * b
    return result
