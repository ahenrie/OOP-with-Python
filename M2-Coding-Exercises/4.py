class Dancer:
  def __init__(self, name, nationality, style):
    self._name = name
    self._nationality = nationality
    self._style = style

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    self._name = value

  @property
  def nationality(self):
    return self._nationality

  @nationality.setter
  def nationality(self, value):
    self._nationality = value

  @property
  def style(self):
    return self._style

  @style.setter
  def style(self, value):
    self._style = value

my_dancer = Dancer("Savion Glover", "American", "tap")
print(my_dancer.name)
print(my_dancer.nationality)
print(my_dancer.style)

my_dancer.name = 'Anna Pavlova'
my_dancer.nationality = 'Russian'
my_dancer.style = 'ballet'

print(my_dancer.name)
print(my_dancer.nationality)
print(my_dancer.style)
