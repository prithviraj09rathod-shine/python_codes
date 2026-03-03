class solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left_pointer = 0
        max_length = 0

        for right_pointer in range(len(s)):
            current_char = s[right_pointer]

            while s[right_pointer] in char_set:
                char_set.remove(s[left_pointer])
                left_pointer += 1

            char_set.add = char_set[current_char] + 1

            char_set.add(s[right_pointer])
            max_length = max(max_length, right_pointer - left_pointer + 1)

        return max_length
obj = solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(obj.lengthOfLongestSubstring("bbbbb"))     # Output: 1
