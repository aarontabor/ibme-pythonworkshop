from functions import hypoteneus
from random import randint

class Point:

  '''
  This is called a "constructor" method.
  It will be called when we create an "instance" of this class (e.g., p = Point()).
  '''
  def __init__(self, x=0, y=0):
    # self is a "magic" keyword that refers to the newly created object.
    self.x = x
    self.y = y
  
  '''
  This is an "instance method". We can tell by the first `self` parameter.
  Instance methods can only be called by "instances" of the class (i.e., objects).
  Note that the `self` argument is provided implicitly by python (e.g., p1.distance_to(p2) # no `self` required) 
  '''
  def distance_to(self, another_point):
    delta_x = abs(self.x - another_point.x)
    delta_y = abs(self.y - another_point.y)
    return hypoteneus(delta_x, delta_y)
  
  '''
  This is a "class function". We can tell because it doesn't have the `self` parameter.
  Class functions are called through the class (e.g., p = Point.generate_random_point())
  '''
  def generate_random_point():
    max_val = 100
    x = randint(0, max_val)
    y = randint(0, max_val)
    return Point(x, y)

  '''
  This is called a "dunder" method.
  Dunder methods are used to control how our classes work with built-in language features.
  The `__str__` method is called when python tries to convert the class to a string (e.g., print(p)).
  '''
  def __str__(self):
    return f'Point({self.x}, {self.y})'
