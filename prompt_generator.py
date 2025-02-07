from all_words import word_dictionary
import random

prompt_list = [n for n in word_dictionary if len(set(n)) == 7]

def generate_prompt():
    prompt = random.choice(prompt_list)

    return prompt