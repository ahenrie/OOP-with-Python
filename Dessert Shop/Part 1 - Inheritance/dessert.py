class DessertItem:
  def __init__(self, name):
    self.name = name

class Candy(DessertItem):
  def __init__(self, name, cand_weight, price_per_pound):
    super().__init__(name)
    self.cand_weight = cand_weight
    self.price_per_pound = price_per_pound

class Cookie(DessertItem):
  def __init__(self, name, cookie_quantity, price_per_dozen):
    super().__init__(name)
    self.cookie_quantity = cookie_quantity
    self.price_per_dozen = price_per_dozen

class IceCream(DessertItem):
  def __init__(self, name, scoop_count, price_per_scoop):
    super().__init__(name)
    self.scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop

class Sundae(IceCream):
  def __init__(self, name, topping_name, topping_price):
    super().__init__(name, None, None)
    self.topping_name = topping_name
    self.topping_price = topping_price
