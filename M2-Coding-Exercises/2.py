class Artist:
  def __init__(self, name, medium, style, famous_artwork):
    self.__name = name
    self.__medium = medium
    self.__style = style
    self.__famous_artwork = famous_artwork

my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')
print(my_artist._Artist__name)
print(my_artist._Artist__medium)
print(my_artist._Artist__style)
print(my_artist._Artist__famous_artwork)
