from abc import (ABC, abstractmethod)
from packaging import Packaging
from payable import Payable
from combine import Combinable

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

  def __eq__(self, other):
    return self.calculate_cost() == other.calculate_cost()

  def __ne__(self, other):
    return self.calculate_cost() != other.calculate_cost()

  def __lt__(self, other):
    return self.calculate_cost() < other.calculate_cost()

  def __gt__(self, other):
    return self.calculate_cost() > other.calculate_cost()

  def __ge__(self, other):
    return self.calculate_cost() >= other.calculate_cost()

  def __le__(self, other):
    return self.calculate_cost() <= other.calculate_cost()


class Candy(DessertItem):
  def __init__(self, name, candy_weight, price_per_pound, packaging = "Bag"):
    super().__init__(name)
    self.candy_weight = candy_weight
    self.price_per_pound = price_per_pound
    self.packaging = packaging
  
  def calculate_cost(self):
    return round(self.candy_weight * self.price_per_pound, 2)

  #def __str__(self):
  #  return f"{self.name} ({self.packaging})\n      {self.candy_weight}lbs. @ ${self.price_per_pound:.2f}/lb:\t\t\t${self.calculate_cost():.2f}\t\t[Tax: ${self.calculate_tax():.2f}]"
  
  def __str__(self):
    return f"{self.name}, {self.packaging}, {self.candy_weight}lbs, ${self.price_per_pound:.2f}, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"

  def can_combine(self, other: "Candy") -> bool:
    if isinstance(other, Candy) and other.name == self.name and other.price_per_pound == self.price_per_pound:
      return True
    else:
      return False

  def combine(self, other: "Candy") -> "Candy":
    if self.can_combine(other):
      self.candy_weight = self.candy_weight + other.candy_weight
    else:
      pass

class Cookie(DessertItem):
  def __init__(self, name, cookie_quantity, price_per_dozen, packaging = "Box"):
    super().__init__(name)
    self.cookie_quantity = cookie_quantity
    self.price_per_dozen = price_per_dozen
    self.packaging = packaging
  
  def calculate_cost(self):
    return round(self.cookie_quantity * (self.price_per_dozen / 12), 2)
  
  #def __str__(self):
  #  return f"{self.name} ({self.packaging})\n      {self.cookie_quantity} cookies @ ${self.price_per_dozen:.2f}/dozen:\t\t\t${self.calculate_cost():.2f}\t\t[Tax: ${self.calculate_tax():.2f}]"
  def __str__(self):
    return f"{self.name}, {self.packaging}, {self.cookie_quantity} cookies, ${self.price_per_dozen:.2f}, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"

  def can_combine(self, other: "Cookie") -> bool:
    if isinstance(other, Cookie) and other.name == self.name and other.price_per_dozen == self.price_per_dozen:
      return True
    else:
      return False

  def combine(self, other: "Cookie") -> None:
    if self.can_combine(other):
      self.cookie_quantity += other.cookie_quantity

class IceCream(DessertItem):
  def __init__(self, name, scoop_count, price_per_scoop, packaging = "Bowl"):
    super().__init__(name)
    self.scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop
    self.packaging = packaging
  
  def calculate_cost(self):
    return round(self.scoop_count * self.price_per_scoop, 2)
  
  #def __str__(self):
  #  return f"{self.name} ({self.packaging})\n      {self.scoop_count} scoops @ ${self.price_per_scoop:.2f}/scoop:\t\t\t${self.calculate_cost():.2f}\t\t[Tax: ${self.calculate_tax():.2f}]"

  def __str__(self):
    return f"{self.name}, {self.packaging}, {self.scoop_count} scoops, ${self.price_per_scoop:.2f}, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}"

class Sundae(IceCream):
  def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price, packaging = "Boat"):
    super().__init__(name, scoop_count, price_per_scoop)
    self.topping_name = topping_name
    self.topping_price = topping_price
    self.packaging = packaging
  
  def calculate_cost(self):
    return round((self.scoop_count * self.price_per_scoop) + (self.topping_price), 2)

  #def __str__(self):
  #  return f"{self.name} Sundae ({self.packaging})\n      {self.scoop_count} scoops @ ${self.price_per_scoop:.2f}/scoop:\n      {self.topping_name} @ ${self.topping_price:.2f}:\t\t\t${self.calculate_cost():.2f}\t\t[Tax: ${self.calculate_tax():.2f}]"

  def __str__(self):
    return f"{self.name}, {self.packaging}, {self.scoop_count} scoops, ${self.price_per_scoop:.2f}, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}, {self.topping_name}, ${self.topping_price:.2f}"

class Order(Payable):
  def __init__(self):
    self.order = []      
    self.set_pay_type("CASH")

  def add(self, item):
    if not any(existing_item.can_combine(item) for existing_item in self.order):
      self.order.append(item)
    else:
      for existing_item in self.order:
        if existing_item.can_combine(item):
          existing_item.combine(item)
          break
  

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

  def sort(self):
    self.order.sort()

  def __str__(self):
    return f"Order Subtotals, "", "", "", ${order_cost:.2f}, ${order_tax:.2f}"
    """
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
    """

class Customer:
  def __init__(self, customer_name, order_history, customer_id):
    self.customer_name = customer_name
    self.order_history = []
    self.customer_id = customer_id

  def add2history(self, order: Order) -> "Customer":
    self.order_history.append(order)
    return self
