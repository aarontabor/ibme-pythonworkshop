'''
namedtuples are readable and user-friendly way to work with tuples.
'''

# one way to represent color is with an 'rgb' value
# (three integers in the range [0,255] representing 'red', 'green', and 'blue' saturation)
red = (255, 0, 0)
blue = (0, 0, 255)

# However, this isn't exactly a user-friendly / readable format
print(red)
print(blue)

# Items are only accessible by their index. This is also not ideal.
def blend(color1, color2):
  return (
    (color1[0]+color2[0]) / 2,
    (color1[1]+color2[1]) / 2,
    (color1[2]+color2[2]) / 2,
  )

purple = blend(red, blue)
print(purple)


# We can use namedtuples to make this more readable
from collections import namedtuple
Color = namedtuple('Color', ['r', 'g', 'b'])

# named tuples allow us to code more explicitly
red = Color(r=255, g=0, b=0)
blue = Color(r=0, g=0, b=255)

# ...and are more explicit when debugging
print(red)
print(blue)

# namedtuples are backwards compatible with built-in tuples
blend(red, blue)

