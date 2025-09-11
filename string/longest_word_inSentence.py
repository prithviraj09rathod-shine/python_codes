def longest_word(sentence):
    words = sentence.split()
    print(type(words))
    print(words)
    longest = max(words, key=len)
    return longest
# Example usage
sentence = "The quick brown fox jumped over the lazy dog"
print("Longest word in the sentence is:", longest_word(sentence))  # Output: "jumped"