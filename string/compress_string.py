from itertools import groupby

def compress_string(s):
    compressed_list = []
    for char, group in groupby(s):
        count = len(list(group))
        compressed_list.append(f"{char}{count}")
        print(compressed_list)
    return ''.join(compressed_list)  

# Example usage:
s = "aaabbbccdaa"
print(compress_string(s))  # Output: "a3b3c2d1a2"
s = "abcd"
#print(compress_string(s))  # Output: "a1b1c1d1
