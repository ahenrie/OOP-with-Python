import unittest
from dessert import Candy, DessertItem, Cookie, IceCream, Sundae

class TestDessertItems(unittest.TestCase):
  def test_IceCream(self):
    testCream = IceCream("Vanilla", 3, 2.50)
    self.assertEqual(testCream.name, "Vanilla")
    self.assertEqual(testCream.scoop_count, 3)
    self.assertEqual(testCream.price_per_scoop, 2.50)
    #test calculate_cost
    self.assertEqual(testCream.calculate_cost(), 3 * 2.50)
    #test calculate_tax
    self.assertEqual(testCream.calculate_tax(), (3 * 2.50) * 0.0725)

if __name__ == '__main__':
    unittest.main()
