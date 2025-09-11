from itertools import permutations

""" def find_all_permutations(s):
    if len(s) == 0:
        return ['']
    
    permutations = []
    for i, char in enumerate(s):
        # Get all permutations of the string without the current character
        for perm in find_all_permutations(s[:i] + s[i+1:]):
            permutations.append(char + perm)
    
    return permutations """

def find_all_permutations1(s):
    return [''.join(p) for p in permutations(s)]

print(find_all_permutations1("abc"))
#print(find_all_permutations("abc"))
#print(find_all_permutations("aab"))  # To see how it handles duplicates