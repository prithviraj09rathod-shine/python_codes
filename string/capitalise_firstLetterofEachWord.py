def capitalise_firstLetter_of_eachWord(s):
    words = s.split()
    print(words)
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

# Example usage:
s = "hello world! this is a test."
s1 = "hello"
print(capitalise_firstLetter_of_eachWord(s1))  # Output: "Hello World! This Is A Test."
s = "python programming language"
print(capitalise_firstLetter_of_eachWord(s))  # Output: "Python Programming Language

def capitalise_firstLetter_of_eachWord1(s):
    #text = "hello word from python" 
    c = s.title() #use title function to capitalise first letter of each word in multiple words
    return c


s = "hello word from python."
print(capitalise_firstLetter_of_eachWord1(s))  # Output: "Hello World! This Is A Test."  
