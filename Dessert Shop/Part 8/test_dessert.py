import pytest
from dessert import Candy

def test_dessertitem_relational_operators():
  # Create two candy objects with different prices
  candy1 = Candy("Chocolate Bar", 0.2, 1.99)
  candy2 = Candy("Gummy Bears", 0.3, 0.99)
  candy3 = Candy("Lil Bears", 12, 12)

  ################Test ==################
  assert candy1 == candy1
  assert candy1 != candy2

  ################Test <################
  assert candy2 < candy1 

  ################Test <=################
  assert candy1 <= candy3 

  ################# Test >################
  assert candy3 > candy1

  ################ Test >=################
  assert candy1 >= candy1  
  assert candy3 >= candy2
