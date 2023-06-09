import pytest
from dessert import Order, Candy, Cookie, IceCream

def test_order():
  order = Order()
  order.add(Candy("Chocolate", 0.1, 1.1))
  order.add(Cookie("Chocolate Chip", 1000, 10))
  order.add(IceCream("Strawberry", 2, 4))

  order.sort()

  list_of_items = list(order)

  for i in range(len(list_of_items)-1):
    assert list_of_items[i].calculate_cost() <= list_of_items[i+1].calculate_cost()
