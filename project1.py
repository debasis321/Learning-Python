import json
from difflib import get_close_matches # helps to get close matching words
dictionary = json.load(open("dictionary.json"))

def Meanit(query):
    if query in dictionary:
        meaning = dictionary[query]
        return meaning
    elif len(get_close_matches(query, dictionary.keys(), 1)) > 0: # close matching founded
        match = get_close_matches(query, dictionary.keys(), 1)[0];
        YN = input("Do you mean to say %s. If Yes PRESS Y else N" %match)
        return YN
    else:  # no close matching
        return "Try again"

q = input("Type the unknown Word: ")
print(Meanit(q))
