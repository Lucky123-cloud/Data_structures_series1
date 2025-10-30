def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total

# Example usage:
if __name__ == "__main__":
    number = 12345
    print(f"The sum of digits in {number} is {sum_of_digits(number)}")