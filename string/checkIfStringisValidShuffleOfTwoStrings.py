from collections import Counter

def is_valid_shuffle1(s, s1, s2):
    if len(s) != len(s1) + len(s2):
        return False
    count_s = Counter(s)
    count_s1_s2 = Counter(s1) + Counter(s2)
    return count_s == count_s1_s2

def is_valid_shuffle2(s, s1, s2):
    if len(s) != len(s1) + len(s2):
        return False
    return sorted(s1+s2) == sorted(s)

def is_valid_shuffle(s, s1, s2):
    if len(s) != len(s1) + len(s2):
        return False

    i = j = k = 0

    while k < len(s):
        if i < len(s1) and s[k] == s1[i]:
            i += 1
        elif j < len(s2) and s[k] == s2[j]:
            j += 1
        else:
            return False
        k += 1
    return True


# Example usage:
s = "aadbbc"
r = "aadbbcbcac"
s1 = "abc"
s2 = "adb"
print(is_valid_shuffle(s, s1, s2))  # Output: True
print(is_valid_shuffle1(r, s1, s2))  # Output: True
print(is_valid_shuffle2(s, s1, s2))  # Output: True
s = "aadbbbaccc"
s1 = "abc"  
s2 = "adb"
print(is_valid_shuffle2(s, s1, s2))  # Output: False