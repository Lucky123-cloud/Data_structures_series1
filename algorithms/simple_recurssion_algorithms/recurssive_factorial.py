def recursive_factorial(n):
    """Calculate the factorial of a non-negative integer n using a recursive approach.

    Args:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the given integer n. If n is 0, returns 1. """
    
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)