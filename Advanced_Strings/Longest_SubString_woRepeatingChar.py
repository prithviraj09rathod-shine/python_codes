def longest_substring_without_repeating_char(s):
    char_index_map = {}
    start = max_length = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length


def longest_substring_without_repeating_char1(s):
    char_index_map = {}
    start = max_length = 0

    for i, char in enumerate(s):
        if char in char_index_map:
            start = max(start, char_index_map[char] + 1)
        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Example usage:
s = "abcabcbb"
print(longest_substring_without_repeating_char(s))  # Output: 3 ("abc")
s = "bbbbb"
print(longest_substring_without_repeating_char(s))  # Output: 1 ("b
s = "pwwkew"
print(longest_substring_without_repeating_char1(s))  # Output: 3 ("wke")