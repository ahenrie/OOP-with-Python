my_string = "polymorphism"
num1 = 3
num2 = 5
print(num1 * num2)
print(my_string * num1)

num1 = 3
num2 = 5
print(int.__mul__(num1, num2))


class FinancialAccount:
  def __init__(self, amount):
    self.account = amount
    
  def __add__(self, other):
    return self.account + other.account
    
class BankAccount(FinancialAccount):
  pass

class InvestmentAccount(FinancialAccount):
  pass

my_banking = BankAccount(500)
my_investments = InvestmentAccount(750)
print(my_investments + my_banking)
