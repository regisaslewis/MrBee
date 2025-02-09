import random
from all_words import word_dictionary
from prompt_generator import generate_prompt

random_prompt = generate_prompt()
prompt_necessity = random.choice(random_prompt)


def find_words(necessary_letter, prompt):
    broad_search = [n for n in word_dictionary if len(n) >= 4 and necessary_letter in n]
    prompt_letters = [n for n in prompt]
    answers_list = []
    points = 0

    for n in broad_search:
        letters = [x for x in n]
        if set(letters).issubset(prompt_letters):
            answers_list.append(n)
    
    pangrams = [n for n in answers_list if set(n) == set(prompt_letters)]
    
    for n in answers_list:
        if len(set(n)) == 7:
            points += (7 + len(n))
        elif len(n) == 4:
            points += 1
        else:
            points += len(n)


    print(f"All words: {answers_list}")
    print(f"Number of acceptable words: {len(answers_list)}")
    print(f"All pangrams: {pangrams}")
    print(f"Total points: {points}")
    print(f"|{prompt_necessity.upper()}| {set([n for n in prompt if n != prompt_necessity])}")


find_words(prompt_necessity, random_prompt)