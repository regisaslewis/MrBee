import random
from player_guess_pickle import player_guess, show_points, read_guesses, today
from results import find_words, find_pangrams, find_points
from prompt_collection import prompt_collection

def main():

    sample_letters = prompt_collection.get(today)
    necessary_letter = sample_letters[0]
    optional_letters = [n for n in sample_letters if n != necessary_letter]
    possible_points = find_points(necessary_letter, sample_letters)
    win_condition = 100 if possible_points > 300 else (possible_points / 3)
    grats_unshown = True

    print(f"Letters for {today}: |{necessary_letter.upper()}| {optional_letters}")
    print(f"Total Possible Points: {possible_points}")
    print(f"Your Current Points: {show_points()}")
    print(f"Points to Genius: {win_condition}")
    print("Enter 1 to see your words.")
    print("Enter 2 to shuffle.")
    print("Enter 0 to quit.")
    print("=============")
    while True:
        player_choice = input("Enter a word: ")    
        if player_choice == "0":
            print("Good Bye!")
            exit()
        elif player_choice == "1":
            print(f"{show_points()} of {win_condition} points in {len(read_guesses()[today])} word{'' if len(read_guesses()[today]) == 1 else 's'}:")
            print("None yet" if len(read_guesses()[today]) == 0 else sorted(read_guesses()[today]))
            print("=============")
            print(f"|{necessary_letter.upper()}| {optional_letters}")
        elif player_choice == "2":
            random.shuffle(optional_letters)
            print("Shuffling...")
            print("=============")
            print(f"|{necessary_letter.upper()}| {optional_letters}")
        elif player_choice == "54532":
            print(find_words(necessary_letter, sample_letters))
            print(find_pangrams(necessary_letter, sample_letters))
        else:
            player_guess(sample_letters, necessary_letter, player_choice.lower())
            print("=============")
            print(f"|{necessary_letter.upper()}| {optional_letters}")
        if show_points() >= win_condition and grats_unshown:
            print("We have ourselves a genius!")
            print("Enter 0 to finish or keep going!")
            grats_unshown = False

if __name__ == "__main__":
    main()