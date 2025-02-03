from all_words import word_list

word = "alphabet"

if word in word_list:
    print(f"{word} found at position {word_list.index(word)}")
else:
    print("Word not found.")