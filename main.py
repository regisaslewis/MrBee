with open ("all_words.json", "r") as all_words:
    word_list = all_words.read()

word = "animal"

if word in word_list:
    print(f"'{word}:' found it!")
else:
    print(f"'{word}' not found")