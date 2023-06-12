import unittest
from dessert import Candy, DessertItem, Cookie, IceCream, Sundae, Order

class TestOrder(unittest.TestCase):
#Test CARD
  def test_with_candy(self):
    ordertest1 = Order()
    ordertest1.set_pay_type("CARD")
    self.assertEqual(ordertest1.get_pay_type(), "CARD")

#Test CASH
  def test_with_candy(self):
    ordertest2 = Order()
    ordertest2.set_pay_type("CASH")
    self.assertEqual(ordertest2.get_pay_type(), "CASH")
  
#Test PHONE
  def test_with_candy(self):
    ordertest3 = Order()
    ordertest3.set_pay_type("PHONE")
    self.assertEqual(ordertest3.get_pay_type(), "PHONE")

#Test CASH as default
  def test_with_candy(self):
    ordertest = Order()
    self.assertEqual(ordertest.get_pay_type(), "CASH")


if __name__ == '__main__':
    unittest.main()
