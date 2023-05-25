#####Display Memory Location of Object#####
class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    
my_dog = Dog('Rocky', 'Pomeranian')
print(my_dog)

#####Display Description with Function#####
class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def describe(self):
    print(f"{self.name} is a {self.breed}")

my_dog = Dog('Rocky', 'Pomeranian')
my_dog.describe()

#####Display Description "Pythonic" Way#####
class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def __str__(self):
    return f'{self.name} is a {self.breed}'

my_dog = Dog('Rocky', 'Pomeranian')
print(my_dog)
my_dog.__str__()

####################__repr__####################
class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    
  def __str__(self):
    return f'{self.name} is a {self.breed}'
  
  def __repr__(self):
    return f'Dog({self.name}, {self.breed})'
    
my_dog = Dog('Rocky', 'Pomeranian')
print(repr(my_dog))

###############################################
class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    
  def __str__(self):
    return f'{self.name} is a {self.breed}'
    
dogs = []
dogs.append(Dog('Rocky', 'Pomeranian'))
dogs.append(Dog('Bullwinkle', 'Labrador Retriever'))
print(dogs)
###############################################
class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    
  def __repr__(self):
    return f'Dog({self.name}, {self.breed})'
    
dogs = []
dogs.append(Dog('Rocky', 'Pomeranian'))
dogs.append(Dog('Bullwinkle', 'Labrador Retriever'))
print(dogs)
