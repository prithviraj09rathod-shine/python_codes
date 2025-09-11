def is_only_digit(s):
    return s.isdigit()

# Example usage
print(is_only_digit("12345"))  # True
print(is_only_digit("123a45")) # False
print(is_only_digit(" "))      # False