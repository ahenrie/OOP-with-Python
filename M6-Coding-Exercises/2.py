#Displaying objects as strings using different methods
class Band:
  def __init__(self, name, genre, members):
    self.name = name
    self.genre = genre
    self.members = members
    
  def __str__(self):
    return f"{self.name} is a {self.genre} band."

  def __repr__(self):
   return f'Band({self.name}, {self.genre}, {self.members})'

dead = Band('The Grateful Dead', 'rock\'n roll', ['Jerry', 'Bob', 'Mickey', 'Bill', 'Phil', 'Pigpen'])

print(dead)
print(repr(dead))
