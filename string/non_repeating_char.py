from collections import Counter

def non_repeating_char(s):
    char_count = {}
    
    # Count the occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
    return None

def first_non_repeating_char1(s):
    freq = Counter(s)
    #freq = dict(Counter(s))
    print(freq)
    for char in s:
        if freq[char] == 1:
            return char
    return None

def non_repeating_char1(s):
    result_list = []
    freq = Counter(s)
    #freq = dict(Counter(s))
    print(freq)
    for char in s:
        if freq[char] == 1:
            result_list.append(char)  
    return result_list

# Example usage:
s = "swiss"
print(non_repeating_char(s))  # Output: "w"
s = "relevel"
print(non_repeating_char1(s))  # Output: ['r', 'v']