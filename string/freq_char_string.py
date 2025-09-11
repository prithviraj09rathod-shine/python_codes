
from collections import Counter

def freq_char(string1):
    #string1 = "banana"
    freq = {}
    for char in string1:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def freq_char1(string2):
    return dict(Counter(string2))

print(freq_char("banana"))
print(freq_char("hello"))

print("freq_char:", freq_char1("BANANA"))