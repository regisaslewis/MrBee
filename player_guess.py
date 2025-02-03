from all_words import word_list
successful_guesses = []

def player_guess(word, guess):
    word_letters = [n for n in word]
    guess_letters = [n for n in guess]
    unusable_letters = [n for n in guess_letters if n not in word_letters]
    if unusable_letters:
        print(f"Unacceptable letters: {sorted(set(unusable_letters), key=unusable_letters.index)}")
        return False
    if word[0] not in guess:
        print(f"Necessary letter |{word[0].upper()}| not used in '{guess}.')")
        return False
    if len(guess) < 4:
        print(f"{guess}: Too few letters provided.")
        return False
    if guess not in word_list:
        print(f"'{guess}' is not found in our dictionary.")
        return False
    if guess in successful_guesses:
        print(f"'{guess}' is already used.")
        return False
    else:
        successful_guesses.append(guess)
        print(f"{guess}: Success!")
        return True