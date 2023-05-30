import unittest
from dessert import Candy, DessertItem, Cookie, IceCream, Sundae

class TestDessertItems(unittest.TestCase):
#Test concrete subclass with cost and tax
  def test_with_candy(self):
    candy = Candy("Chocolate Bar", 0.5, 1.99)
    self.assertEqual(candy.name, "Chocolate Bar")
    self.assertAlmostEqual(candy.calculate_cost(), 0.5 * 1.99, places=2)
    self.assertAlmostEqual(candy.calculate_tax(), (0.5 * 1.99) * (candy.tax_percentage / 100), places=2)
    #test tax_percentage
    self.assertEqual(candy.tax_percentage, 7.25)

#Test inheritance 
  def test_inheritance(self):
    self.assertTrue(issubclass(Candy, DessertItem))
    self.assertTrue(issubclass(Cookie, DessertItem))
    self.assertTrue(issubclass(IceCream, DessertItem))
    self.assertTrue(issubclass(Sundae, DessertItem))
    self.assertTrue(issubclass(Sundae, IceCream))

if __name__ == '__main__':
    unittest.main()
