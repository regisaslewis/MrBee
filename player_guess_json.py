from all_words import word_dictionary
from datetime import date
import json

today = date.today().strftime("%Y-%m-%d")

def read_guesses():
    with open("sg_db.json", "r") as f:
        data = json.load(f)
        dict = json.loads(data)
        if today not in dict:
            dict.update({today: []})
    return dict

successful_guesses = read_guesses()

def update_sg():
    with open("sg_db.json", "w") as f:
        json_sg = json.dumps(successful_guesses)
        json.dump(json_sg, f)

def player_guess(word, necessary_letter, guess):
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
    if guess in successful_guesses[today]:
        print(f"'{guess}' was already used.")
        return False
    if len(set(guess)) == 7:
        successful_guesses[today].append(guess)
        update_sg()
        print(f"{guess}: Now that's a PANGRAM!!")
        print(f"Your Points: {show_points()}")
        return True
    successful_guesses[today].append(guess)
    update_sg()
    print(f"{guess}: Success!")
    print(f"Your Points: {show_points()}")
    return True

def show_points():
    points = 0
    for n in successful_guesses[today]:
        if len(set(n)) == 7:
            points += (7 + len(n))
        elif len(n) > 4:
            points += len(n)
        else:
            points += 1
    return points