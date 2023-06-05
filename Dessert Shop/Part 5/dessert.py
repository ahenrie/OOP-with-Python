from abc import (ABC, abstractmethod)

class DessertItem(ABC):
  def __init__(self, name):
    self.name = name
    self.tax_percent = 7.25
  
  @abstractmethod
  def calculate_cost(self):
    pass
  
  def calculate_tax(self):
    return round(self.calculate_cost() * (self.tax_percent / 100), 2)

class Candy(DessertItem):
  def __init__(self, name, candy_weight, price_per_pound):
    super().__init__(name)
    self.candy_weight = candy_weight
    self.price_per_pound = price_per_pound
  
  def calculate_cost(self):
    return round(self.candy_weight * self.price_per_pound, 2)

  def __str__(self):
    return f"{self.name}, {self.candy_weight}lbs, ${self.price_per_pound:.2f}/lb, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"


class Cookie(DessertItem):
  def __init__(self, name, cookie_quantity, price_per_dozen):
    super().__init__(name)
    self.cookie_quantity = cookie_quantity
    self.price_per_dozen = price_per_dozen
  
  def calculate_cost(self):
    return round(self.cookie_quantity * (self.price_per_dozen / 12), 2)
  
  def __str__(self):
    return f"{self.name}, {self.cookie_quantity} cookies, ${self.price_per_dozen:.2f}/dozen, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"

class IceCream(DessertItem):
  def __init__(self, name, scoop_count, price_per_scoop):
    super().__init__(name)
    self.scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop
  
  def calculate_cost(self):
    return round(self.scoop_count * self.price_per_scoop, 2)
  
  def __str__(self):
    return f"{self.name}, {self.scoop_count} scoops, ${self.price_per_scoop:.2f}/scoop, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"

class Sundae(IceCream):
  def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
    super().__init__(name, scoop_count, price_per_scoop)
    self.topping_name = topping_name
    self.topping_price = topping_price
  
  def calculate_cost(self):
    return round((self.scoop_count * self.price_per_scoop) + (self.topping_price), 2)

  def __str__(self):
    return f"{self.name}, {self.scoop_count} scoops, ${self.price_per_scoop:.2f}/scoop, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}, {self.topping_name}, 1, ${self.topping_price:.2f}"

class Order:
  def __init__(self):
    self.order = []      
   
  def add(self, item):
    self.order.append(item)
   
  def __len__(self):
    return len(self.order)
   
  def __iter__(self):
    return iter(self.order)
   
  def __next__(self):
    return self.order.__next__()
  
  def order_cost(self):
    total = 0
    for item in self.order:
      total += item.calculate_cost()
    return total
  
  def order_tax(self):
    total_tax = 0
    for item in self.order:
      total_tax += item.calculate_tax()
    return total_tax

  def __str__(self):
    terminal = ""
    for item in self.order:
      terminal += str(item) + "\n"
    return terminal
