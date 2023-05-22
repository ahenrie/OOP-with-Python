"""
Operator	Method Name
+	object.__add__(self, other)
-	object.__sub__(self, other)
*	object.__mul__(self, other)
/	object.__truediv__(self, other)
//	object.__floordiv__(self, other)
<	object.__lt__(self, other)
<=	object.__le__(self, other)
==	object.__eq__(self, other)
!=	object.__ne__(self, other)
>	object.__gt__(self, other)
>=	object.__ge__(self, other)
"""
class FinancialAccount:
  def __init__(self, amount):
    self.account = amount
    
  def __eq__(self, other):
    return self.account == other.account
    
class BankAccount(FinancialAccount):
  pass

class InvestmentAccount(FinancialAccount):
  pass

my_banking = BankAccount(500)
my_investments = InvestmentAccount(750)
print(my_investments == my_banking)

class FinancialAccount:
  def __init__(self, amount):
    self.account = amount
    
  def __truediv__(self, other):
    return self.account / other.account
    
class BankAccount(FinancialAccount):
  pass

class InvestmentAccount(FinancialAccount):
  pass

my_banking = BankAccount(500)
my_investments = InvestmentAccount(750)
print(my_investments / my_banking)

class FinancialAccount:
  def __init__(self, amount):
    self.account = amount
    
  def __floordiv__(self, other):
    return self.account // other.account
  
class BankAccount(FinancialAccount):
  pass

class InvestmentAccount(FinancialAccount):
  pass

my_banking = BankAccount(500)
my_investments = InvestmentAccount(750)
print(my_investments // my_banking)

class Alpha:
  def __init__(self, value):
    self.value = value

  def __gt__(self, other):
    return self.value > other.value

class Bravo(Alpha):
  pass

class Charlie(Alpha):
  pass

example1 = Bravo(10)
example2 = Charlie(7)

print(example1 > example2)


