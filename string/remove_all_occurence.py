def removeAllOccurrences(s, charToRemove):
    return s.replace(charToRemove, '')  
# Example usage:
s = "hello world"   
charToRemove = 'o'
print(removeAllOccurrences(s, charToRemove))  # Output: "hell wrld"

def removeAllOccurrences1(s, charToRemove):
    result = ''.join([char for char in s if char != charToRemove])
    return result
# Example usage:
s = "hello world"
charToRemove = 'l'
print(removeAllOccurrences1(s, charToRemove))  # Output: "heo word"
