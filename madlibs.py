#maya clark
# a simulation of the popular madlibs game where silly stories are generated using input from the player

#initialize
import random

random_nouns = ["dog", "cat", "book", "fish", "car", "house" ]
random_verbs = ["ran", "jumped", "slept", "ate", "thought", "coded"]
random_adjectives = ["happy", "sad", "angry", "funny", "big", "small"]
random_places = ["park", "school", "bedroom", "moon", "store", "ocean"]

print("welcome to the python madlibs game! enter the prompts to create a fun story")

noun1 = input("enter a noun: ")
verb1 = input("enter a verb: ")
adjective1 = input("enter an adjective: ")
place1 = input("enter a place: ")

noun2 = random.choice(random_nouns)
verb2 = random.choice(random_verbs)
adjective2 = random.choice(random_adjectives)
place2 = random.choice(random_places)

B = "\033[1m"
E = "\033[0m"

f_noun1 = f"{B}{noun1.upper()}{E}"
f_verb1 = f"{B}{verb1.upper()}{E}"
f_adjective1 = f"{B}{adjective1.upper()}{E}"
f_place1 = f"{B}{place1.upper()}{E}"
f_noun2 = f"{B}{noun2.upper()}{E}"
f_verb2 = f"{B}{verb2.upper()}{E}"
f_adjective2 = f"{B}{adjective2.upper()}{E}"
f_place2 = f"{B}{place2.upper()}{E}"

story = f"""
{B}---Your Completed Story---{E}
Once upon a time, a {f_adjective1} {f_noun1} decided to {f_verb1} all the way to the {f_place1}.
On their journey, they stumbled across a {f_noun2}.
Together they became good friends and planned to meet up that next Saturday at the {f_place2}.
{f_noun1} was so {f_adjective2} that he {f_verb2} all the way home
"""
#main
print(story)
