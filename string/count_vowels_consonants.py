def count_vowels_consonants(s: str) -> tuple:
    vowels = "aeiouAEIOU"
    """ v_count = sum(1 for char in s if char in vowels)
    c_count = sum(1 for char in s if char.isalpha() and char not in vowels) """
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1

    return v_count, c_count 

print(count_vowels_consonants("Reshma"))
print(count_vowels_consonants("banana"))