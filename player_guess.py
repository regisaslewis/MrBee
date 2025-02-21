from all_words import word_dictionary
successful_guesses = []

def player_guess(word, necessary_letter, guess):
    global points 
    word_letters = [n for n in word]
    guess_letters = [n for n in guess]
    unusable_letters = [n for n in guess_letters if n not in word_letters]
    if unusable_letters:
        print(f"Unacceptable letters: {sorted(set(unusable_letters), key=unusable_letters.index)}")
        return False
    if necessary_letter not in guess:
        print(f"Necessary letter |{necessary_letter.upper()}| not used in '{guess}.')")
        return False
    if len(guess) < 4:
        print(f"{guess}: Too few letters provided.")
        return False
    if guess not in word_dictionary:
        print(f"'{guess}' is not found in our dictionary.")
        return False
    if guess in successful_guesses:
        print(f"'{guess}' was already used.")
        return False
    if len(set(guess)) == 7:
        successful_guesses.append(guess)
        print(f"{guess}: Now that's a PANGRAM!!")
        print(f"Your Points: {points}")
        return True
    successful_guesses.append(guess)
    print(f"{guess}: Success!")
    print(f"Your Points: {points}")
    return True

def show_points():
    points = 0
    for n in successful_guesses:
        if len(set(n)) == 7:
            points += (7 + len(n))
        elif len(n) > 4:
            points += len(n)
        else:
            points += 1
    return points