def reverse_words(s):
    # Step 1: Remove leading/trailing spaces
    s = s.strip()
    
    # Step 2: Split the string into words
    words = s.split()
    
    # Step 3: Reverse the list of words
    reversed_words = words[::-1]
    
    # Step 4: Join them back into a single string
    return ' '.join(reversed_words)

input_str = "  Hello   world  from  Python  "
output_str = reverse_words(input_str)
print("Reversed:", output_str)
#Reversed: Python from world Hello
