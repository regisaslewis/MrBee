from all_words import word_dictionary

def find_words(necessary_letter, prompt):
    
    broad_search = [n for n in word_dictionary if len(n) >= 4 and necessary_letter in n]
    prompt_letters = [n for n in prompt]
    answers_list = []

    for n in broad_search:
        letters = [x for x in n]
        if set(letters).issubset(prompt_letters):
            answers_list.append(n)

    return answers_list

def find_pangrams(necessary_letter, prompt):
    prompt_letters = [n for n in prompt]

    return [n for n in find_words(necessary_letter, prompt) if set(n) == set(prompt_letters)]

def find_points(necessary_letter, prompt):
    points = 0

    for n in find_words(necessary_letter, prompt):
        if len(set(n)) == 7:
            points += (7 + len(n))
        elif len(n) == 4:
            points += 1
        else:
            points += len(n)
    
    return points