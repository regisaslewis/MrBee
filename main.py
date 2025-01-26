def word_check(word):
    letters = set([n for n in word])
    if len(letters) < 7:
        return f"'{word}' has too few unique letters."
    if len(letters) > 7:
        return f"'{word}' has too many unique letters."
    return "Acceptable word."

def player_guess(word, guess):
    word_letters = [n for n in word]
    guess_letters = [n for n in guess]
    unusable_letters = [n for n in guess_letters if n not in word_letters]
    if unusable_letters:
        return sorted(set(unusable_letters), key=unusable_letters.index)
    return "Success!"


print("word_check:", word_check("hexagon"))
print("word_check:", word_check("beekeeper"))
print("word_check:", word_check("ambidextrous"))
print("player_guess:", player_guess("hexagon", "gone"))
print("player_guess:", player_guess("hexagon", "fishing"))