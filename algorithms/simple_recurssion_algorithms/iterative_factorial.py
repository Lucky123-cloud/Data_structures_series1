def iterative_factorial(n):
    """Calculate the factorial of a non-negative integer n using an iterative approach.

    Args:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the given integer n. If n is 0, returns 1. """
    
    fact = 1

    for i in range(2, n+1):
        fact *= i
    return fact


# Example usage:
if __name__ == "__main__":
    number = 5
    print(f"The factorial of {number} is {iterative_factorial(number)}")