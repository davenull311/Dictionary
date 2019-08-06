'''
    Program: dictionary.py
    Author: Dave Null
    Date: 7/24/2019
    Purpose: This is a simple dictionary that queries a .json file and returns
            the definition(s) of the word supplied by the user.
'''

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

# Define the function that validates user input, searches the data and returns the appropriate definitions.
def translate(word):
    word = word.lower()

    # Check to see if the input, as spelled, is in the data. If so, return definition.
    if word in data:
        return data[word]

    # If the input is not found, check to see if capitalizing the first letter fixes this...
    elif word.title() in data:
        return data[word.title()]

    # If the input is still not found, check to see if capitalizing all of the letters fixes this...
    elif word.upper() in data:
        return data[word.upper()]

    # If the input is still not found, use the get_close_matches function to suggest similar words.
    elif len(get_close_matches(word, data.keys())) > 0:
        # If a similar word is found, ask the user if that's what they meant to type, and if so display that definition.
        yes_no = input("Did you mean %s instead? [Y]es or [N]o: " % get_close_matches(word, data.keys())[0])
        if yes_no.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        # If the top suggested word isn't what the user intended, display that the word doesn't exist as entered.
        elif yes_no.lower() == "n":
            return "The word doesn't exist. Please double check input."
        #If the user enters something other than yes/no, display that we're confused.
        else:
            return "We don't understand your response..."

    # If none of these techniques found the intended word, display that the word doesn't exist.
    else:
        return "The word doesn't exist. Please double check input."

word = input("Enter word: ")

output = translate(word)

# Remove JSON formatting from the output...
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
