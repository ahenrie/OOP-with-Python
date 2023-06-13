import pytest
from dessert import Candy, Order, Customer

def test_customer():
  customer1 = Customer("Palpatine", [], 66)
  assert customer1.customer_name == "Palpatine"
  assert customer1.customer_id == 66
