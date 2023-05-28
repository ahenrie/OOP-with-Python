class Candy:
  def __init__(self, name, weight, price_per_pound):
    self.name = name
    self.weight = weight
    self.price_per_pound = price_per_pound

class Cookie:
  def __init__(self, name, quantity, price_per_dozen):
    self.name = name
    self.quantity = quantity
    self.price_per_dozen = price_per_dozen

class IceCream:
  def __init__(self, name, scoop_count, price_per_scoop):
    self.name = name
    self. scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop

class Sundae:
  def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
    self.name = name
    self.scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop
    self.topping_name = topping_name
    self.topping_price = topping_price
