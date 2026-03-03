'''
class solution:
    def isMatch(self, s:str, p:str)->bool:
        cache = {}
        def dfs(i,j):
            if (i, j ) in cache:
                return cache[(i,j)]
            if i>= len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            match = i<len(s) and (s[j]==p[j] or p[j]==".")
            if (j+1) < len(p) and p[j+1]=="*" :
                cache[(i,j)] = dfs(i, j+2) or (match and dfs(i+1, j))

                return cache[(i, j)]
            
            if match:
                cache[((i,j))] = dfs(i+1, j+1)
                return cache[(i, j)]
            cache[(i,j)] = False
            return False
        return dfs(0,0)
    
obj = solution()
s = "aa"
p = "a*"
#output true
#ex2: 
s1="ab"
p1=".*"
s2="aa"
p2="a"

print(obj.isMatch(s, p))
print(obj.isMatch(s1,p1))
print(obj.isMatch(s2, p2))
'''


import re

def is_match(s: str, p: str) -> bool:
    # Use fullmatch to ensure the entire string is matched
    return re.fullmatch(p, s)
print(is_match("aab", "c*a*b"))           # True
print(is_match("mississippi", "mis*is*p*."))  # False
print(is_match("aa", "a*"))               # True
print(is_match("ab", ".*"))    