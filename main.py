from all_words import word_list

word = input("Test word: ")

if word in word_list:
    print(f"'{word}:' found it!")
else:
    print(f"'{word}' not found")