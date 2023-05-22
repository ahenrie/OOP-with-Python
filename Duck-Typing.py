import random

class BaseballPlayer:  
  def hit(self):
    """Generate a random integer 1 to 4 and return the type of hit"""
    total_bases = random.randint(1, 4)
    if total_bases == 1:
      return "single"
    elif total_bases == 2:
      return "double"
    elif total_bases == 3:
      return "triple"
    else:
      return "home run"

class Boxer:
  def hit(self):
    return "jab"
    
class Song:
  def __init__(self, title, ranking):
    self.title = title
    self.ranking = ranking
    
  def hit(self):
    """A song is a hit if it appeared in a top 40 chart"""
    if self.ranking <= 40:
      return f"{self.title} is a hit song"
    else:
      return f"{self.title} is not a hit song"

#Class with no method named "hit"
class Dancer:
  def spin(self):
    return "Spin spin spin"

def print_hit(obj):
  try:
    print(obj.hit())
  except AttributeError as e:
    print(e)

my_dancer = Dancer()
my_boxer = Boxer()
my_player = BaseballPlayer()
my_song = Song("Hey Jude", 12)

print_hit(my_player)
print_hit(my_song)
print_hit(my_boxer)
print_hit(my_dancer) #--> AttributeError: 'Dancer' object has no attribute 'hit'

#####################################################################################################################
class Bird:
  def fly(self):
    return "I am flapping my wings"
  
class Car:
  def drive(self):
    return "My wheels are turning"

def print_fly(obj):
  try:
    print(obj.fly())
  except AttributeError as e:
    print(e)

bird = Bird()
car = Car()
print_fly(bird)
print_fly(car)
