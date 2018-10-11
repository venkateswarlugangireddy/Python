import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translation(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = raw_input("did you mean %s instead? if yes type Y or N if no:" % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "the word doesn't exist, please double check it"
        else:
            return "we didn't understand your entry"

    else:
        return "word doesn't exists, please check again"


word = raw_input("Enter word: ")  # type: object

output = translation(word)

if type(output) == list:
    for item in output:
        print item
else:
    print(output)

