# parent classes
class Person:
  def __init__(self, name, address):
    self.name = name
    self.address = address
    
  def get_info(self):
    return f"{self.name} lives at {self.address}."
  
class CardHolder:
  def __init__(self, account_number):
    self.account_number = account_number
    self.balance = 0
    self.credit_limit = 5000
    
  def process_sale(self, price):
    self.balance += price
    
  def make_payment(self, amount):
    self.balance -= amount
    
# declare child class here
class PlatinumClient(Person, CardHolder):
  def __init__(self, name, address, account_number, cash_back = 0.02, rewards = 0):
    Person.__init__(self, name, address)
    CardHolder.__init__(self, account_number)
    self.cash_back = cash_back
    self.rewards = rewards

  def process_sale(self, price):
    self.rewards += price * self.cash_back
    self.balance += price

platinum = PlatinumClient("Sarah", "101 Main Street", 123364)
platinum.process_sale(100)
print(platinum.rewards)
print(platinum.balance)
platinum.make_payment(50)
print(platinum.balance)
print(platinum.get_info())
