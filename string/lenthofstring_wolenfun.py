def string_length_without_len(s):
    count = 0
    for char in s:
        count += 1
    return count    

# Example usage:
s = "Hello, World!"
print(string_length_without_len(s))  # Output: 13