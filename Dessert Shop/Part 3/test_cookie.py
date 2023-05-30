import unittest
from dessert import Candy, DessertItem, Cookie, IceCream, Sundae

class TestDessertItems(unittest.TestCase):
  def test_cookie(self):
    testCookie = Cookie("Chocolate Chip", 2, 5.99)
    self.assertEqual(testCookie.name, "Chocolate Chip")
    self.assertEqual(testCookie.cookie_quantity, 2)
    self.assertEqual(testCookie.price_per_dozen, 5.99)
    #test calculate_cost
    self.assertEqual(testCookie.calculate_cost(), 2 * 5.99/12)
    #test calculate_tax
    self.assertEqual(testCookie.calculate_tax(), (2 * 5.99/12) * 0.0725)

if __name__ == '__main__':
    unittest.main()
