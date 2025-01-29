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
        print(f"{guess}:  Too few letters provided.")
        return False
    if guess in successful_guesses:
        print(f"'{guess}' is already used.")
        return False
    else:
        successful_guesses.append(guess)
        print(f"{guess}: Success!")
        return True

test_word = input("Test sample validity: ")

sample_letters = sorted(set([n for n in test_word]), key=test_word.index)

if word_check(test_word):
    necessary_letter = sample_letters[0]
    optional_letters = sample_letters[1:]
    print(f"Use these letters: |{necessary_letter.upper()}| {optional_letters}")
    print("Enter 0 to quit.")
    print("Enter 1 to see your words.")
    while True:
        player_choice = input("Enter a word: ")
        if player_choice == "0":
            print("Good Bye!")
            exit()
        if player_choice == "1":
            print(successful_guesses)
        else:
            player_guess(sample_letters, player_choice)