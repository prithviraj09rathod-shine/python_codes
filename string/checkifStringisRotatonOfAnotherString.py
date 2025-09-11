def checkStringRotation(s1, s2):
       return len(s1) == len(s2) and s2 in (s1 + s1)

# Example usage:
s1 = "waterbottle"
s2 = "erbottlewat"
print(checkStringRotation(s1, s2))  # Output: True
s1 = "hello"
s2 = "llohe"
print(checkStringRotation(s1, s2))  # Output: True