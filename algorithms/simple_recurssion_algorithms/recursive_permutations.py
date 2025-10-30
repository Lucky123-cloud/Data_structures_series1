def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            current_char = string[i]
            remaining_chars = string[:i] + string[i+1:]
            permute(remaining_chars, pocket + current_char)

# Example usage:
if __name__ == "__main__":
    input_string = "ABC"
    print(f"All permutations of the string '{input_string}':")
    permute(input_string)