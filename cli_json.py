import random
from player_guess_json import player_guess, show_points, read_guesses, today
from results import find_words, find_pangrams, find_points
from prompt_collection import prompt_collection

def main():
    sample_letters = prompt_collection.get(today)
    necessary_letter = sample_letters[0]
    optional_letters = [n for n in sample_letters if n != necessary_letter]
    possible_points = find_points(necessary_letter, sample_letters)
    win_condition = 100 if possible_points > 300 else (possible_points / 3)
    grats_unshown = True
    cheated = False

    print(f"Letters for {today}: |{necessary_letter.upper()}| {optional_letters}")
    print(f"Total Possible Points: {possible_points}")
    print(f"Your Current Points: {show_points()}")
    print(f"Points to Genius: {win_condition}")
    print("Enter 1 to see your words.")
    print("Enter 2 to shuffle.")
    print("Enter 0 to quit.")
    while True:
        print("=============")
        print(f"|{necessary_letter.upper()}| {optional_letters}")
        player_choice = input("Enter a word: ")    
        if player_choice == "0":
            if cheated:
                print("Good Bye, CHEATER!")
            else:
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
            cheated = True
            print("*********************")
            print("Welcome to cheating!")
            print("Enter 1 for today's prompt.")
            print("Or enter your own prompt")
            print("(the first letter will be the necessary one)")
            print("(no)")
            print("Enter 0 to return to the game.")
            print("*********************")
            answers_search = input("Enter prompt: ")
            if answers_search == "1":
                print(f"Words: {find_words(necessary_letter, sample_letters)}")
                print(f"Pangrams: {find_pangrams(necessary_letter, sample_letters)}")
            elif answers_search == "0":
                pass
            else:
                cheat_prompt = [n for n in answers_search.lower()]
                if len(set(cheat_prompt)) == 7:
                    print(f"Words: {find_words(cheat_prompt[0], cheat_prompt)}")
                    print(f"Pangrams: {find_pangrams(cheat_prompt[0], cheat_prompt)}")
                    print(f"Total possible points: {find_points(cheat_prompt[0], cheat_prompt)}")
                else:
                    print("Not 7 valid letters.")
            print("Returning to the game...")
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