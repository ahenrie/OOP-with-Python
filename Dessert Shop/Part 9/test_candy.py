import pytest
from dessert import Candy, DessertItem, Cookie, IceCream, Sundae

def test_can_comnine():
  candy1 = Candy("Chocolates", 1, 2)
  candy2 = Candy("Chocolates", 232, 2)
  assert candy1.can_combine(candy2) is True

def test_candy_noncandy():
  candy1 = Candy("Chocolates", 1, 2)
  cookie1 = Cookie("Chocolate Chip", 1, 2)
  assert candy1.can_combine(cookie1) is False

def test_candy_add():
  candy1 = Candy("Chocolates", 1, 2)
  candy2 = Candy("Chocolates", 232, 2)
  candy1.combine(candy2)
  assert candy1.candy_weight == 233 #1 + 232 = 233

def test_candy_nonadd():
  candy1 = Candy("Chocolates", 1, 2)
  cookie1 = Cookie("Chocolate Chip", 1, 2)
  assert candy1.candy_weight == 4 #1 + 1 = 2 FAIL
