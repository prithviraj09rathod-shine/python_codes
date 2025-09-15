def checkIfAllCharUniqueinString(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return False
        char_set.add(char)
    return True

def checkIfAllCharUniqueinString1(s):
    return len(s) == len(set(s))

# Example usage:
s = "abcdefg"
print(checkIfAllCharUniqueinString(s))  # Output: True
s = "hello"
print(checkIfAllCharUniqueinString1(s))  # Output: False


