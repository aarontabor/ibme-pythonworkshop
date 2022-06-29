'''
A Basic Function
'''
import math

def hypoteneus(a, b):
  return math.sqrt(a**2 + b**2)

# print(hypoteneus(3, 4))



'''
Arguments can be specified positionally or by using keywords.
Default values can be provided. This allows the caller to omit the argument when calling
'''
def greet_user(name, language='en'):
  greetings = {
    'en': 'Hello',
    'fr': 'Bonjour',
  }
  
  supported_languages = greetings.keys()
  if language not in supported_languages:
    raise Exception # later, I'll show you how to make a custom exception

  greeting = greetings[language]
  return f'{greeting} {name}'

# print(greet_user('Aaron')) # defaults to english
# print(greet_user('Aaron, language='fr'))



'''
A common idiom in python programming is to code "optimistically".
'''
def greet_user_handle_exception(name, language='en'):
  greetings = {
    'en': 'Hello',
    'fr': 'Bonjour',
  }
  
  try:
    greeting = greetings[language]
  except KeyError:
    print('[INFO] Unrecognized language key provided - Falling back to english as default.')
    greeting = greetings['en']

  return(f'{greeting} {name}')

# print(greet_user('Aaron, language='sp')) # Handles unsupported languages gracefully



'''
Functions can be assigned to variables.
Functions can also accepts functions as arguments.
'''
def last_letter_sorting_key(s):
  return s[-1].lower()

import random
def wacky_sorting_key(s):
  letters = list('abcdefghijklmnopqrstuvwxyz')
  random.shuffle(letters)
  return letters.index(s[0].lower())

names = 'Ian Aaron Evan Shri'.split()
# print(sorted(names)) # uses conventional 'lexographical' sort order
# print(sorted(names, key=last_letter_sorting_key))
# print(sorted(names, key=wacky_sorting_key))


'''
Sometimes, we really only need a single-use function.
We can define a funtion inline using the `lambda` keyword.
'''
sorted(names, key=lambda s: s[-1])


'''
A `generator` is a function that "remembers" its execution progress between calls.
We can tell this is a generator because of the `yield` keyword.
`yield` tells python to pause execution, resuming again when the function is called again.
'''
def simple_range_generator(stop):
  current = 1
  while current < stop:
    yield current
    current += 1

# my_range = simple_range_generator(3)
# my_range.__next__()
# my_range.__next__()
# my_range.__next__()
# my_range.__next__() # We've exhausted the generator. This will raise a `StopIteration` exception.

# # For-loops know how to handle ranges implicitly
# for i in simple_range_generator(5):
#   print(i)

