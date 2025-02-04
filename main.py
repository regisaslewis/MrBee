import random

list = ["a", "b", "c", "d", "e", "f", "g"]
necessary_item = random.choice(list)
optional_items = [n for n in list if n != necessary_item]

print(necessary_item)
print(optional_items)