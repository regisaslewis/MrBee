def word_check(word):
    letters = set([n for n in word])
    if len(letters) < 7:
        print(f"'{word}' has too few unique letters.")
        return False
    if len(letters) > 7:
        print(f"'{word}' has too many unique letters.")
        return False
    print("Acceptable word.")
    return word