def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""
    
    start, max_length = 0, 1
    
    for i in range(n):
        # Odd length palindromes
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > max_length:
                start = l
                max_length = r - l + 1
            l -= 1
            r += 1
        
        # Even length palindromes
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > max_length:
                start = l
                max_length = r - l + 1
            l -= 1
            r += 1
    
    return s[start:start + max_length]

# Example usage:
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"
s = "cbbd"
print(longest_palindromic_substring(s))  # Output: "bb"
s = "a"
print(longest_palindromic_substring(s))  # Output: "a"