
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def longest_common_prefix1(strs):
    #strs = ["flower","flow","flight"]
    if not strs:
        return ""
    
    min_str = min(strs,key=len)
    print("min string:",min_str)
    max_str = max(strs,key=len)
    print("max string:",max_str)

    for i, char in enumerate(min_str):
        print(enumerate[i], char)
        if char != max_str[i]:
            return min_str[:i]
    
            
#print(longest_common_prefix(["flower","flow","flight"])) #fl
#print(longest_common_prefix1(["dog","racecar","car"])) #"" #"" no common prefix
print(longest_common_prefix1(["flower","flow","flight"])) #fl