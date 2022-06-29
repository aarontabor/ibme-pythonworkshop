'''
KeyErrors are annoying.
Often, we have a consistent initial value in mind.
`default_dict` allows us to provide a default for all missing keys
'''
from collections import defaultdict


def count_letter_occurences(s):
  counts = {}
  for letter in s:
    if letter not in counts.keys():
      counts[letter] = 0
    counts[letter] += 1
  return counts


def better_count_letter_occurences(s):
  counts = defaultdict(int) # initializes missing keys to a new integer (i.e., 0)
  for letter in s:
    counts[letter] += 1
  return counts

# s = 'asdfasdagsaddgasdfasdffffffffffasdfasdfasd'
# print(count_letter_occurences(s))
# print(better_count_letter_occurences(s))


## Just for fun, we can print out a report ordered by frequency
def print_frequency_report(counts):
  def sort_by_values(element):
    k, v = element
    return v
  
  for letter, frequency in sorted(counts.items(), key=sort_by_values, reverse=True):
    print(letter, frequency)