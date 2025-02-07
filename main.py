from all_words import word_dictionary

prompt_dictionary = dict.fromkeys([n for n in word_dictionary if len(set(n)) == 7], 1)

def prompt_checker(word):

    if word in prompt_dictionary:
        return f"{word} found"
    else: 
        return f"{word} not found"
    
print(prompt_checker("hexagon"))
print(prompt_checker("hexagonal"))
print(prompt_checker("lifeline"))
print(prompt_checker("spraining"))