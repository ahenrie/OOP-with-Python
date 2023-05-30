from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self, name, tax_percentage=7.25):
        self.name = name
        self.tax_percentage = tax_percentage

    @abstractmethod
    def calculate_cost(self):
      pass
    
    def calculate_tax(self):
      return self.calculate_cost() * (self.tax_percentage / 100)

   
   #pythonic of representing an object in string form
    def __str__(self):
        return self.name

class Candy(DessertItem):
  def __init__(self, name, cand_weight, price_per_pound):
    super().__init__(name)
    self.cand_weight = cand_weight
    self.price_per_pound = price_per_pound

  def calculate_cost(self):
    return self.cand_weight * self.price_per_pound

class Cookie(DessertItem):
  def __init__(self, name, cookie_quantity, price_per_dozen):
    super().__init__(name)
    self.cookie_quantity = cookie_quantity
    self.price_per_dozen = price_per_dozen

  def calculate_cost(self):
    return self.cookie_quantity * (self.price_per_dozen/12)

class IceCream(DessertItem):
  def __init__(self, name, scoop_count, price_per_scoop):
    super().__init__(name)
    self.scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop

  def calculate_cost(self):
    return self.scoop_count * self.price_per_scoop

class Sundae(IceCream):
  def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
    super().__init__(name, scoop_count, price_per_scoop)
    self.topping_name = topping_name
    self.topping_price = topping_price

  #super() used to ensure the correct order in MRO
  def calculate_cost(self):
    return super().calculate_cost() + self.topping_price

class Order:
   def __init__(self):
      self.order = []
      self.cost = 0

   def add(self, item):
      self.order.append(item)
      self.cost += item.calculate_cost()

   def order_cost(self):
     return self.cost

   def order_tax(self):
     total_tax = 0
     for item in self.order:
       total_tax += item.calculate_tax()
     return total_tax
   
   def __len__(self):
      return len(self.order)

   def __iter__(self):
      self.index = 0
      return self

   def __next__(self):
      if self.index < len(self.order):
         item = self.order[self.index]
         self.index += 1
         return item
      else:
         raise StopIteration

   def __str__(self):
      return f'Total number of items in order: {(self.__len__)()}'
