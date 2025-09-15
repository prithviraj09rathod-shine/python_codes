def convertoUpperCase_wofun(s):
    result = ''
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase by adjusting ASCII value
            upper_char = chr(ord(char) - (ord('a') - ord('A')))
            result += upper_char
        else:
            result += char  # Non-lowercase characters remain unchanged
    return result

def converttoUpperCase(s):
    result = s.upper()
    print(result) 
    return result

# Example usage:
s = "Hello, World!"
print(convertoUpperCase_wofun(s))  # Output: "HELLO,
print(convertoUpperCase_wofun("python3.8"))  # Output: "PYTHON3.8"
