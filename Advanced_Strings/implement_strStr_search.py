def implement_strStr(haystack, needle):
    if not needle:
        return 0
    needle_length = len(needle)
    for i in range(len(haystack) - needle_length + 1):
        if haystack[i:i + needle_length] == needle:
            return i
    return -1

# Example usage:
haystack = "hello"
needle = "ll"
print(implement_strStr(haystack, needle))  # Output: 2  
haystack = "aaaaa"
needle = "bba"
print(implement_strStr(haystack, needle))  # Output: -1
haystack = ""
needle = ""
print(implement_strStr(haystack, needle))  # Output: 0
haystack = "a"
needle = "a"
print(implement_strStr(haystack, needle))  # Output: 0