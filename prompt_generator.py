from all_words import word_dictionary
import random
import datetime

prompt_list = [n for n in word_dictionary if len(set(n)) == 7]

def generate_prompt():
    prompt = random.choice(prompt_list)

    return prompt

today = datetime.date.today()
prompt_dictionary = {}

for n in range(30):
    sample_letters = sorted(set([n for n in generate_prompt()]))
    random.shuffle(sample_letters)
    prompt_dictionary.update({(today + datetime.timedelta(days = n)).strftime("%Y-%m-%d"): sample_letters})

print(prompt_dictionary)