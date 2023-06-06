import unittest
from dessert import Candy, DessertItem, Cookie, IceCream, Sundae

class TestDessertItems(unittest.TestCase):
  def test_Sundae(self):
    testSundae = Sundae("Banana Split", 3, 2.50, "Nuts", 1.5, "Boat")
    self.assertEqual(testSundae.name, "Banana Split")
    self.assertEqual(testSundae.scoop_count, 3)
    self.assertEqual(testSundae.price_per_scoop, 2.50)
    self.assertEqual(testSundae.topping_name, "Nuts")
    self.assertEqual(testSundae.topping_price, 1.5)
    self.assertEqual(testSundae.packaging, "Boat")
  

if __name__ == '__main__':
    unittest.main()
