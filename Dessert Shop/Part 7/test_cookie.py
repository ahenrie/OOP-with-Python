import unittest
from dessert import Candy, DessertItem, Cookie, IceCream, Sundae

class TestDessertItems(unittest.TestCase):
  def test_candy(self):
    testCandy = Candy("Twix", 10, 1.5, "Bag")
    self.assertEqual(testCandy.name, "Twix")
    self.assertEqual(testCandy.candy_weight, 10)
    self.assertEqual(testCandy.price_per_pound, 1.5)
    self.assertEqual(testCandy.packaging, "Bag")


if __name__ == '__main__':
    unittest.main()
