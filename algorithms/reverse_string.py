def reverse_string(s):
    return s[::-1]


# Example usage:
if __name__ == "__main__":
    test_string = "Hello, World!"
    print(f"Original String: {test_string}")
    print(f"Reversed String: {reverse_string(test_string)}")


def  reverse_string2(s):
    reversed_string = ""

    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


# Example usage:
if __name__ == "__main__":
    test_string = "Python is fun!"
    print(f"Original String: {test_string}")
    print(f"Reversed String: {reverse_string2(test_string)}")