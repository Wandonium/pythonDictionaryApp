"""
This project uses the json library to read data from a json file. The data is a python dictionary containing a large number of words along with their definitions. Hence it can be used to create a simple cli dictionary of common english words and phrases.
The project can handle words in upper, lower and mixed cases.
The project can also handle misspelled words up to a point by using the difflib library
"""

import json
from difflib import get_close_matches

def get_def(word):
  data = json.load(open('data.json'))
  word = word.lower()
  if word in data:
    definition = data[word]
    return definition
  elif word.title() in data: #if user entered "texas" or "TEXAS" this will check for "Texas" as well.
    return data[word.title()]
  elif word.upper() in data:  #in case user enters words like USA or NATO
    return data[word.upper()]
  elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
    yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
    if yn == "Y":
      correctWord = get_close_matches(word, data.keys())[0]
      return data[correctWord]
    elif yn == 'N':
      return "The word doesn't exist. Please double check it."
    else:
      return 'We did not understand your entry.'
  else:
    return "The word doesn't exist. Please double check it."

word = input('Enter a word to get its definition:')
output = (get_def(word))
if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)