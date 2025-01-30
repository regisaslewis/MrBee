from word_check import word_check
from player_guess import player_guess, successful_guesses

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