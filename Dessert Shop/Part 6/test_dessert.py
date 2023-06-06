import unittest
from dessert import Candy, DessertItem, Cookie, IceCream, Sundae

class TestDessertItems(unittest.TestCase):
#Test concrete subclass with cost and tax
  def test_with_candy(self):
    candy = Candy("Chocolate Bar", 0.5, 1.99, "Bag")
    self.assertEqual(candy.name, "Chocolate Bar")
    self.assertEqual(candy.packaging, "Bag")

#Test inheritance 
  def test_inheritance(self):
    self.assertTrue(issubclass(Candy, DessertItem))
    self.assertTrue(issubclass(Cookie, DessertItem))
    self.assertTrue(issubclass(IceCream, DessertItem))
    self.assertTrue(issubclass(Sundae, DessertItem))
    self.assertTrue(issubclass(Sundae, IceCream))

if __name__ == '__main__':
    unittest.main()
