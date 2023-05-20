class Person:
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, new_name):
    if type(new_name) != str:
      raise TypeError("Names have to be strings. Name not changed.")
      self.name = self.name
    else:
      self._name = new_name
    
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, new_age):
    if new_age < 1:
      self.age = self.age
      raise TypeError("Ages have to be posetive")
    else:
      self._age = new_age
  
c = Person("Calvin", "6")
print(c.name)
print(c.age)
c.age = -17
c.name = "False"
print(c.name)
print(c.age)
