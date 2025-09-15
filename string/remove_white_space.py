def remove_whiteSpaces(s):
    return ''.join(s.split())   
print(remove_whiteSpaces("  Hello   World  "))  # Output: "HelloWorld"

#without split function
def remove_whiteSpaces1(s):
    result = ''.join([char for char in s if char != ' '])
    return result
print(remove_whiteSpaces1("  Hello   World  "))  # Output: "HelloWorld"