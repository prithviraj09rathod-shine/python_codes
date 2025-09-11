#check iftwo strings are anagrams are not
def are_anagrans(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    print(str1)
    str2 = str2.replace(" ", "").lower()
    print(str2)
    # If lengths differ, they cannot be anagrams
    if len(str1) != len(str2):
        return False
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)

# Example usage
string1 = "Listen"
string2 = "Silent"
string3 = "Hello"
result = are_anagrans(string1, string2)

print(f"Are '{string1}' and '{string2}' anagrams? {result}")    
print(f"Are '{string1}' and '{string3}' anagrams? {are_anagrans(string1, string3)}") 
