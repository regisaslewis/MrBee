from all_words import word_dictionary
word = input("Test word: ")

if word in word_dictionary:
    print(f"'{word}:' found it!")
else:
    print(f"'{word}' not found")