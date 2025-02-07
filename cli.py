import random
from player_guess import player_guess, successful_guesses
from prompt_generator import generate_prompt

sample_letters = sorted(set([n for n in generate_prompt()]))
necessary_letter = random.choice(sample_letters)
optional_letters = [n for n in sample_letters if n != necessary_letter]

print(f"Use these letters: |{necessary_letter.upper()}| {optional_letters}")
print("Enter 0 to quit.")
print("Enter 1 to see your words.")
print("Enter 2 to shuffle.")
print("=============")
while True:
    player_choice = input("Enter a word: ")
    if player_choice == "0":
        print("Good Bye!")
        exit()
    elif player_choice == "1":
        print("Your words:")
        print(sorted(successful_guesses))
        print("=============")
        print(f"|{necessary_letter.upper()}| {optional_letters}")
    elif player_choice == "2":
        random.shuffle(optional_letters)
        print("Shuffling...")
        print("=============")
        print(f"|{necessary_letter.upper()}| {optional_letters}")
    else:
        player_guess(sample_letters, necessary_letter, player_choice.lower())
        print("=============")
        print(f"|{necessary_letter.upper()}| {optional_letters}")