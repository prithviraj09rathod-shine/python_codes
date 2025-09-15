def capitalise_firstLetter_of_eachWord(s):
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

# Example usage:
s = "hello world! this is a test."
print(capitalise_firstLetter_of_eachWord(s))  # Output: "Hello World! This Is A Test."
s = "python programming language"
print(capitalise_firstLetter_of_eachWord(s))  # Output: "Python Programming Language

def capitalise_firstLetter_of_eachWord1(s):
    text = "hello word from python" 
    c = text.title() #use title function to capitalise first letter of each word in multiple words
    return c


s = "hello world! this is a test."
print(capitalise_firstLetter_of_eachWord1(s))  # Output: "Hello World! This Is A Test."  
