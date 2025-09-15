#split string into words without using split function
def split_string_without_split(s):
    words = []
    current_word = []
    
    for char in s:
        if char == ' ':
            if current_word:  # Avoid adding empty words for multiple spaces
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    
    if current_word:  # Add the last word if there is one
        words.append(''.join(current_word))
    
    return words

# Example usage:
s = "This is a sample string"
print(split_string_without_split(s))  # Output: ['This', 'is', 'a
#sample', 'string']
s = "  Leading and trailing spaces  "
print(split_string_without_split(s))  # Output: ['Leading', 'and', 'trailing', 'spaces']