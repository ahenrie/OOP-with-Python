import unittest
from dessert import Candy, DessertItem, Cookie, IceCream, Sundae

class TestDessertItems(unittest.TestCase):
  def test_candy(self):
    testCandy = Candy("Twix", 10, 1.5)
    self.assertEqual(testCandy.name, "Twix")
    self.assertEqual(testCandy.cand_weight, 10)
    self.assertEqual(testCandy.price_per_pound, 1.5)
    #test calculate_cost
    self.assertEqual(testCandy.calculate_cost(), 10 * 1.5)
    #test calculate_tax
    self.assertEqual(testCandy.calculate_tax(), (10 * 1.5) * 0.0725)

if __name__ == '__main__':
    unittest.main()
