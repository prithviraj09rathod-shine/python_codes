#check iftwo strings are anagrams are not
def are_anagrans(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    # If lengths differ, they cannot be anagrams
    if len(str1) != len(str2):
        return False
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)

def are_anagrans1(str1, str2):
    from collections import Counter
    # Remove spaces and convert to lowercase
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # If lengths differ, they cannot be anagrams
    if len(str1) != len(str2):
        return False
    # Use Counter to count character frequencies and compare
    return Counter(str1) == Counter(str2)

# Example usage
string1 = "Liste n"
string2 = "Silen t"

string3 = "Hello"
result = are_anagrans(string1, string2)

#print(f"Are '{string1}' and '{string2}' anagrams? {result}")    
#print(f"Are '{string1}' and '{string3}' anagrams? {are_anagrans(string1, string3)}") 
result1 = are_anagrans1(string1, string2)
print(f"Are '{string1}' and '{string2}' anagrams? {result1}")
