import unittest
from dessert import Candy, DessertItem, Cookie, IceCream, Sundae

class TestDessertItems(unittest.TestCase):
  def test_candy(self):
    testCandy = Candy("Twix", 10, 1.5)
    self.assertEqual(testCandy.name, "Twix")
    self.assertEqual(testCandy.cand_weight, 10)
    self.assertEqual(testCandy.price_per_pound, 1.5)

  def test_DesertItem(self):
    testDessert = DessertItem("The Best")
    self.assertEqual(testDessert.name, "The Best")

  def test_cookie(self):
    testCookie = Cookie("Chocolate Chip", 2, 5.99)
    self.assertEqual(testCookie.name, "Chocolate Chip")
    self.assertEqual(testCookie.cookie_quantity, 2)
    self.assertEqual(testCookie.price_per_dozen, 5.99)

  def test_IceCream(self):
    testCream = IceCream("Vanilla", 3, 2.50)
    self.assertEqual(testCream.name, "Vanilla")
    self.assertEqual(testCream.scoop_count, 3)
    self.assertEqual(testCream.price_per_scoop, 2.50)

  def test_Sundae(self):
    testSundae = Sundae("Banana Split", 3, 2.50, "Nuts", 1.5)
    self.assertEqual(testSundae.name, "Banana Split")
    self.assertEqual(testSundae.scoop_count, 3)
    self.assertEqual(testSundae.price_per_scoop, 2.50)
    self.assertEqual(testSundae.topping_name, "Nuts")
    self.assertEqual(testSundae.topping_price, 1.5)
  

  def test_inheritance(self):
      self.assertTrue(issubclass(Candy, DessertItem))
      self.assertTrue(issubclass(Cookie, DessertItem))
      self.assertTrue(issubclass(IceCream, DessertItem))
      self.assertTrue(issubclass(Sundae, DessertItem))
      self.assertTrue(issubclass(Sundae, IceCream))

if __name__ == '__main__':
    unittest.main()
