from abc import (ABC, abstractmethod)
from packaging import Packaging
from payable import Payable

class DessertItem(ABC, Packaging):
  def __init__(self, name, packaging: str = None):
    #super().__init__(packaging)
    self.name = name
    self.tax_percent = 7.25
  
  @abstractmethod
  def calculate_cost(self):
    pass
  
  def calculate_tax(self):
    return round(self.calculate_cost() * (self.tax_percent / 100), 2)

class Candy(DessertItem):
  def __init__(self, name, candy_weight, price_per_pound, packaging = "Bag"):
    super().__init__(name)
    self.candy_weight = candy_weight
    self.price_per_pound = price_per_pound
    self.packaging = packaging
  
  def calculate_cost(self):
    return round(self.candy_weight * self.price_per_pound, 2)

  def __str__(self):
    return f"{self.name} ({self.packaging})\n      {self.candy_weight}lbs. @ ${self.price_per_pound:.2f}/lb:\t\t\t${self.calculate_cost():.2f}\t\t[Tax: ${self.calculate_tax():.2f}]"


class Cookie(DessertItem):
  def __init__(self, name, cookie_quantity, price_per_dozen, packaging = "Box"):
    super().__init__(name)
    self.cookie_quantity = cookie_quantity
    self.price_per_dozen = price_per_dozen
    self.packaging = packaging
  
  def calculate_cost(self):
    return round(self.cookie_quantity * (self.price_per_dozen / 12), 2)
  
  def __str__(self):
    return f"{self.name} ({self.packaging})\n      {self.cookie_quantity} cookies @ ${self.price_per_dozen:.2f}/dozen:\t\t\t${self.calculate_cost():.2f}\t\t[Tax: ${self.calculate_tax():.2f}]"

class IceCream(DessertItem):
  def __init__(self, name, scoop_count, price_per_scoop, packaging = "Bowl"):
    super().__init__(name)
    self.scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop
    self.packaging = packaging
  
  def calculate_cost(self):
    return round(self.scoop_count * self.price_per_scoop, 2)
  
  def __str__(self):
    return f"{self.name} ({self.packaging})\n      {self.scoop_count} scoops @ ${self.price_per_scoop:.2f}/scoop:\t\t\t${self.calculate_cost():.2f}\t\t[Tax: ${self.calculate_tax():.2f}]"

class Sundae(IceCream):
  def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price, packaging = "Boat"):
    super().__init__(name, scoop_count, price_per_scoop)
    self.topping_name = topping_name
    self.topping_price = topping_price
    self.packaging = packaging
  
  def calculate_cost(self):
    return round((self.scoop_count * self.price_per_scoop) + (self.topping_price), 2)

  def __str__(self):
    return f"{self.name} Sundae ({self.packaging})\n      {self.scoop_count} scoops @ ${self.price_per_scoop:.2f}/scoop:\n      {self.topping_name} @ ${self.topping_price:.2f}:\t\t\t${self.calculate_cost():.2f}\t\t[Tax: ${self.calculate_tax():.2f}]"

class Order(Payable):
  def __init__(self):
    self.order = []      
    self.set_pay_type("CASH")

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
    terminal = "----------------------------------------------Receipt---------------------------\n"
    for item in self.order:
      terminal += str(item) + "\n"
      cost = item.calculate_cost()
      tax = item.calculate_tax()

    terminal += "---------------------------------------------------------------------------------\n"
    terminal += f"Total items in the order: {len(self.order)}\n"
    terminal += f"Order Subtotals:\t\t\t\t${self.order_cost():.2f}\t\t[Tax: ${self.order_tax():.2f}]\n"
    terminal += f"Order Total:\t\t\t\t\t\t\t      ${self.order_cost() + self.order_tax():.2f}\n"
    terminal += "---------------------------------------------------------------------------------\n"
    terminal += f"Paid with {self.get_pay_type()}"

    return terminal
