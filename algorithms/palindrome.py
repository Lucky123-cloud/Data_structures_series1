def palindrome(s):
    s = s.lower().replace(" ", "")
    reversed_string = s[::-1]
    return s == reversed_string

# Example usage:
if __name__ == "__main__":
    test_string = "racecar"
    if palindrome(test_string):
        print(f"'{test_string}' is a palindrome.")
    else:
        print(f"'{test_string}' is not a palindrome.")


def palindrome2(s):
    reversed_str = ""

    for char in s:
        reversed_str = char + reversed_str
    return s == reversed_str