from all_words import word_list

def word_check(word):
    letters = set([n for n in word])
    if word not in word_list:
        print(f"'{word}' is not found in our dictionary.")
        return False
    if len(letters) < 7:
        print(f"'{word}' has too few unique letters.")
        return False
    if len(letters) > 7:
        print(f"'{word}' has too many unique letters.")
        return False
    print("Acceptable word.")
    return word