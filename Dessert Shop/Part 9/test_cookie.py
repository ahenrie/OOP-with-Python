import pytest
from dessert import Candy, DessertItem, Cookie, IceCream, Sundae

def test_can_combine():
  cookie1 = Cookie("Chocolates", 1, 2)
  cookie2 = Cookie("Chocolates", 2, 2)
  assert cookie1.can_combine(cookie2) is True

def test_candy_noncookie():
  candy1 = Candy("Chocolates", 1, 2)
  cookie1 = Cookie("Chocolate Chip", 1, 2)
  assert candy1.can_combine(cookie1) is False

def test_can_cookieadd():
  cookie1 = Cookie("Chocolates", 1, 2)
  cookie2 = Cookie("Chocolates", 232, 2)
  cookie1.combine(cookie2)
  assert cookie1.cookie_quantity == 233

def test_can_combineFAIL():
  cookie1 = Cookie("Chocolates", 1, 2)
  candy2 = Candy("Chocolates", 500, 2)
  assert cookie1.can_combine(candy2) is True #FAIL
