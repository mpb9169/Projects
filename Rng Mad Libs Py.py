#Rng Mad Libs

import random

stories = [
    {
        "template": "Today I went to the {place}. I saw a {adjective} {noun} that wanted to {verb}!",
        "words": ["place", "adjective", "noun", "verb"]
    },
    {
        "template": "Once upon a time, a {adjective} {animal} lived in the {place}. It loved to {verb} all day.",
        "words": ["adjective", "animal", "place", "verb"]
    },
    {
        "template": "My best friend is a {adjective} {occupation} who can {verb} better than anyone in {place}.",
        "words": ["adjective", "occupation", "verb", "place"]
    }
]

story = random.choice(stories)
user_inputs = {}

for word in story["words"]:
    user_input = input(f"Enter a {word}: ")
    user_inputs[word] = user_input

final_story = story["template"].format(**user_inputs)

print("\nHere's your Mad Libs story:")
print(final_story)

