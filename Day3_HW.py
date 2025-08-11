# 1. Write a function to check whether a given string is a pangram
def is_panagram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
        return True
    
print(is_panagram("The quick brown fox jumps over the lazy dog"))


# 2. Write a function that takes a sentence and returns the word with the maximum length.

def max_length_word(sentence):
    words = sentence.split()
    max_length = 0
    max_length_word = ""
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            max_length_word = word
    return max_length_word

print(max_length_word("I love programming in Python"))


# 3. Write a function to count the number of uppercase and lowercase characters in a string.

def count_upper_lower(str):
    upper_count = 0
    lower_count = 0
    for char in str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

print(count_upper_lower("Hello World"))
